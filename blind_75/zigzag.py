#https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert_grid(self, s: str, numRows: int) -> str:
        if numRows == 1 :
            return s
        grid_rotated = [["" for j in range(numRows)] for i in s[::2]]
        x_loc = -1
        y_loc = 0
        diag = False
        for char in s:
            if not diag:
                x_loc += 1
            else:
                x_loc -= 1
                y_loc += 1
            grid_rotated[y_loc][x_loc] = char
            if x_loc== 0 or len(grid_rotated[0]) - 1:
                diag = not diag
        return "".join(["".join([row[i] for row in grid_rotated]) for i in range(numRows)])

class Solution_list:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""]*numRows
        cursor = 0
        south = False
        for char in s:
            rows[cursor] += char
            if cursor == 0 or cursor == numRows -1:
                south = not south
            cursor += 1 if south else -1
        return ''.join(rows

class Solution_fastest:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 1 or numRows <= 1:
            return s 

        cycle_len = 2 * (numRows - 1)

        rows = [""] * numRows

        for i in range(len(s)):
            position = i % cycle_len
            if position >= numRows:
                position = cycle_len - position
            rows[position] += s[i]

        return "".join(rows))
