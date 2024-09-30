class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # create list of just headers
        headers = [row[0] for row in matrix]

        # binary search headers to find appropriate row
        l = 0
        r = len(headers)-1

        while (l <= r):
            mid = (l+r) // 2

            if (headers[mid] < target):
                l = mid + 1
            elif (headers[mid] > target):
                r = mid - 1
            else:
                return True

        # now binary search row 
        rowToSearch = matrix[(l + r) // 2]
        print(f"searching {rowToSearch}")
        l = 0
        r = len(rowToSearch) - 1

        while (l <= r):
            mid = (l + r) // 2
            if (rowToSearch[mid] < target):
                l = mid + 1
            elif (rowToSearch[mid] > target):
                r = mid - 1
            else:
                return True

        return False
     
