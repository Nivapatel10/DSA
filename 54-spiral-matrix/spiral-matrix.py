class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        while matrix:
            #1. Add first row/list of matrix
            ret+=(matrix.pop(0))

            #2. append last element of all the list in order
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())

            #3. add reverse of last row
            if matrix:
                ret+=(matrix.pop()[::-1])

            #4.append first element of all rows in reverse
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret
            


