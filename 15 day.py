class Solution(object):
    def searchMatrix(self, matrix, target):
        n, m = len(matrix),len(matrix[0])
        target_found = False

        for row in range(n):
            for col in range(m-1, -1, -1):
                if matrix[row][col] == target:
                    target_found = True
                    break
                elif matrix[row][col] > target:
                    continue
                else:
                    break

        return target_found
