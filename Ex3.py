# def sum_matrix(mat1,mat2):
#     if (len(mat1) != len(mat2)) or ((len(mat1[0])) != len(mat2[0])):
#         return 0
#     result=[[0 for i in range(len(mat1[0]))] for i in range(len(mat1)) ]
#     for i in range(len(mat1)):
#         for j in range(len(mat1[0])):
#             result[i][j]= mat1[i][j]+mat2[i][j]
#     return result


def sum_matrix(mat1,mat2):
    if (len(mat1) != len(mat2)) or ((len(mat1[0])) != len(mat2[0])):
        return 0
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat2[i][j]= mat2[i][j] + mat1[i][j]
    return mat2
mat1=[ 
[1,2,3,4],
[2,3,4,5],
[4,5,6,7]]
mat2 = mat1
print(mat1)
print(mat2)
print(sum_matrix(mat1,mat2))
     
