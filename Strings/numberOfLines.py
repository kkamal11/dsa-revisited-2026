from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 0
        curr_line_width_pixel = 0

        for ch in s:
            idx = ord(ch) - ord("a")
            curr_line_width_pixel += widths[idx]
            if curr_line_width_pixel > 100:
                lines += 1
                curr_line_width_pixel = widths[idx]

        if curr_line_width_pixel:
            lines += 1

        return [lines, curr_line_width_pixel]
