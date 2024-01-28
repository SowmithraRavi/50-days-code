class Solution:
    def rotateMatrix(self,N,M,K,Mat):
        K = K % M
        rot= []
        for row in Mat:
            rotated_row = row[K:] + row[:K]
            rot.append(rotated_row)

        return rot
