# This Python file uses the following encoding: utf-8
from __future__ import print_function

# import sys, re


class Table:
    def __init__(self, lines: list[list[str]]) -> None:
        self.rows = lines
        self.columns = lines[0]
        self.max_length = self._get_max_length(lines)

    def _get_max_length(self, lines: list[list[str]]) -> int:
        max_length = 0
        for line in lines:
            for element in line:
                length = len(element)
                if length > max_length:
                    max_length = length
        max_length += 2
        return max_length

    def _hline(self, double: bool = False) -> None:
        if not double:
            dashes = "-" * self.max_length
        else:
            dashes = "=" * self.max_length
        for i in range(0, len(self.columns)):
            print("+", end="")
            print(dashes, end="")
        print("+")

    def _print_table(
        self,
        lines: list[list[str]],
        double_hline: bool = False,
        double_vline: bool = False,
    ) -> None:
        for i in range(0, len(lines)):
            line = lines[i]
            print("|", end="")
            for j in range(0, len(line)):
                element = line[j]
                length = len(element)
                blank_space = self.max_length - length
                left = int((blank_space / 2))
                right = blank_space - left
                print(" " * left, end="")
                print(element, end="")
                if j == 0 and double_vline:
                    print(" " * right, end="‖")
                else:
                    print(" " * right, end="|")
            print()
            self._hline((i == 0 and double_hline))

    def __str__(self) -> str:
        self._hline()
        self._print_table(self.rows)
        return ""


t = Table(
    [
        ["Col 1", "Col 2", "Col 3", "Col 4"],
        ["v11", "v12", "v13", "v14"],
        ["v21", "v22", "v23", "v24"],
    ]
)
print(t)
