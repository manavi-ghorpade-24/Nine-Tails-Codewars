def dir_reduc(arr):
    st = []
    for dir in arr:
        if len(st)>0 and ((st[-1] == "EAST" and dir == "WEST") or (st[-1] == "WEST" and dir == "EAST") or (st[-1] == "NORTH" and dir == "SOUTH") or (st[-1] == "SOUTH" and dir == "NORTH")):
            st.pop()
        else:
            st.append(dir)
    return st