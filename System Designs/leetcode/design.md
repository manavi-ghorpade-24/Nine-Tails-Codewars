# Design LeetCode

A coding platform: browse problems, submit code, run it in isolation, and show results (and a leaderboard).

![LeetCode system design](leetcode%20system%20design.png)

## APIs

| Method | Path | Purpose |
|--------|------|---------|
| `GET`  | `/problems` | List problems |
| `GET`  | `/problems/:id` | Problem statement + code stub |
| `POST` | `/solutions/:uid` | Submit a solution |
| `GET`  | `/check/:id` | Poll until the submission is done |

The client talks only to the **API server**. Judging is asynchronous: submit, then poll.

## Architecture

```text
Client  →  API server  →  Database
                 ↓
               Redis          (leaderboard / hot reads)
                 ↓
               SQS            (submission jobs)
                 ↓
              Worker  →  Docker containers (python, java, sql, html)
                 ↓
           "task complete" back to the API server
```

1. **API server** — auth, CRUD, enqueue run jobs, serve poll results.
2. **Database** — users, problems, submissions, contests.
3. **Redis** — fast reads; sorted sets for ranks (poll ~every 5s, score as the numeric value).
4. **SQS** — buffer between “I submitted” and “a worker can run this.”
5. **Worker + Docker** — pull a job, run user code in a language container, push the verdict back.

## Data model

| Table | Fields |
|-------|--------|
| **User** | profile |
| **Problems** | `problem_id`, code stub, predefined tests / solutions |
| **Solutions** | `user_id`, `problem_id`, source, `language` |
| **Competition** | `competition_id`, `problem_id`s |
| **Competition–user** | score and contest progress |
| **Leadership** | `competition_id`, `user_id`, `score`, `rank` |

## Submission flow

1. `POST /solutions/:uid` stores the code and enqueues `{submission_id, language, source}` on SQS.
2. A worker dequeues, starts the matching Docker image, runs tests under limits.
3. Worker reports **task complete** to the API (verdict, runtime). The API writes the row and updates Redis rank if needed.
4. The client `GET /check/:id` until the status is no longer pending.

SQS keeps the API fast and absorbs spikes (a contest start).

## Sandbox

User code is untrusted. Each run is a container with:

- no (or tiny) **filesystem** access
- **timeouts** so infinite loops die
- **CPU / memory** caps
- **seccomp** (profile via JSON) to block dangerous syscalls

Network: **VPC** + **security groups** (instance: deny inbound by default, allow outbound) and **NACLs** (subnet: lower rule number = higher priority; lock down IPs).

## Insight

Treat “run my code” as a **job**, not a request. The API must not wait on a compiler. Queue + workers + one container per language is the core. Redis sorted sets give `O(log n)` rank updates without scanning the leadership table on every poll.
