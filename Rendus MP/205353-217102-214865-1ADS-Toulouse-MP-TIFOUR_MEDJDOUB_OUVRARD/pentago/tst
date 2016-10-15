from bases import *

array = [[2,1,2],
         [1,0,2],
         [0,0,1]]

N = 3
def rotate_90(N, array):
    result = [[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            result[y][N-1-x] = array[x][y]
    return result
affichage(array)
affichage(rotate_90(N, rotate_90(N, rotate_90(N, array))))
affichage(rotate_90(N, array))
