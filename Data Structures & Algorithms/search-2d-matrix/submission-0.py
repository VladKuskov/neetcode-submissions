class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        clmn = len(matrix[0])
        mid = 0
        l, r = 0, (row * clmn) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid//clmn][mid%clmn] == target:
                return True
            # search the left side, decrement r --> mid - 1
            if target < matrix[mid//clmn][mid%clmn]:
                r = mid - 1
            else:
                l = mid + 1
        return False
        """ex:
        matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
        - row = 3, clmn = 4
        - l, r = 0, 11
        - mid = 5
        
        if matrix[5//4][5%4] == 10:          -->matrix[1][1] = 11
            return true
        if 10 < matrix[5//4][5%4]: (yes, search left)
            r = mid - 1               --> r = 4
            
        REPEAT:
        - l, r = 0, 4
        - mid = 2
        if matrix[2//4][2%4] == 10:          --> matrix[0][2] = 4
        if 10 < matrix[2//4][2%4]:           --> 10 < 4, false, so l = mid + 1, l = 3
        
        REPEAT
        - l, r = 3, 4
        - mid = 3
        
        if matrix[3//4][3%4] == 10:          --> matrix[0][3] = 8
        if 10 < matrix[3//4][3%4]            --> 10 < 8 false, so l = mid + 1, l = 4

        
        REPEAT:
        - l, r = 4, 4
        - mid = 4
        if matrix[4//4][4%4] == 10:          -->matrix[1][0] = 10, FOUND!
            return True
        """