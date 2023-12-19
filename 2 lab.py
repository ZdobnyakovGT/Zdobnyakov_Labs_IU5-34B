def levenstain(slovo1, slovo2):
    a = slovo1
    b = slovo2
    mat = []
    st = []
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            st.append(0)
        mat.append(st)
        st = []

    for i in range(len(b) + 1):
        mat[0][i] = i

    for i in range(len(a) + 1):
        mat[i][0] = i

    m = 1
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                m = 0
            first = mat[i][j - 1] + 1
            second = mat[i - 1][j] + 1
            third = mat[i - 1][j - 1] + m
            mat[i][j] = min(first, second, third)
            m = 1

    for i in range(len(a) + 1):
        print(mat[i])

    return mat[len(a)][len(b)]


sl1 = input()
sl2 = input()

print(levenstain(sl1, sl2))
