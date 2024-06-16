m = 2
n = 3
indices = [[0,1],[1,1]]
def oddCells(m, n, indices):
    matrix = []
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(0)
        matrix.append(temp)
    
    for idx in indices:
        print(idx)
        for i in idx:
            matrix[i]
        
    # print(matrix)
oddCells(m, n, indices)