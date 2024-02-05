def get_magic_triangle(n):
    list = [[1], [1,1]]
    buffer = [1]
    for _ in range(n-2):
        for i in range(len(list[-1]) -1):
            buffer.append(list[-1][i] + list[-1][i+1])
        buffer.append(1)
        list.append(buffer)
        buffer = [1]
    return  list


get_magic_triangle(7)