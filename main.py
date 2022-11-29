"""
Problem: Generate an Identity Matrix of size x size
Description: An Identity Matrix is a 2D Array holding all zeros except a diagonal line from [0][0] to [size - 1][size - 1] that consits of ones
Example: Here is an example of an Identity Matrix of size 4...
[[1, 0, 0, 0],
 [0, 1, 0, 0],
 [0, 0, 1, 0],
 [0, 0, 0, 1]]

Write up your Plan here...
--------------------------
create an empty matrix list...
iterate over a range of n...
  append a list of size n filled with zeros to the matrix...

iterate over a range of n extracting the index i...
  set the content of matrix at the index of [i][i] to one

return matrix to the caller
  

"""


def id_matrix(n):
  matrix = []

  for _ in range(n):
    matrix.append([0] * n)

  for i in range(n):
    matrix[i][i] = 1


  return matrix

print(id_matrix(4))
print(id_matrix(8))
print(id_matrix(16))
