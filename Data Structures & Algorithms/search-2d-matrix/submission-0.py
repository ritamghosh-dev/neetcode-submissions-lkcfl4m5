class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target<=matrix[i][-1]:
                l=0
                r=len(matrix[i])
                while l<r:
                    mid=l+(r-l)//2
                    if matrix[i][mid]==target:
                        return True
                    elif matrix[i][mid]>target:
                        r=mid
                    else:
                        l=mid+1
                return False


        return False

        