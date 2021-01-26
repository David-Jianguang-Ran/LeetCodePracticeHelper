from base import LeetCodeProblem


class Problem(LeetCodeProblem):
    # for behaviours other than exact match between solution output and expected output
    # see # Testers in README.md
    """
    https://leetcode.com/problems/zigzag-conversion/

    ## first try:
    i guess we just append stream to n rows(strings) and add all strings together
    """
    def get_tests(self):
        # return test cases here
        return (
            # each test case has the following structure
            # ( parameter , expected output ),
            # # OR # #
            # ( (param1, param2), expected output ),
            (("", 0), ""),
            (("PA", 20), "PA"),
            (("PA", 2), "PA"),
            (("PAY", 2), "PYA"),
            (("PAY", 3), "PAY"),
            (("PAYPALISHIRING", 1), "PAYPALISHIRING"),
            (("PAYPALISHIRING", 2), "PYAIHRNAPLSIIG"),
            (("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"),
            (("PAYPALISHIRING", 4), "PINALSIGYAHRPI"),
        )

    def solution(self, s, numRows):
        # have fun ~ ^_^
        if numRows == 1:
            return s
        # do zigzag
        working_string = list(s)
        rows = ["" for i in range(numRows)]
        pointer = 0
        going_down = True  # <= going down as in the zigzag pattern
        for each_char in working_string:
            # append char
            rows[pointer] += each_char

            # move pointer
            if going_down:
                if pointer == numRows - 1:
                    pointer -= 1
                    going_down = False
                else:
                    pointer += 1
            else:
                if pointer == 0:
                    pointer += 1
                    going_down = True
                else:
                    pointer -= 1

        # add all rows together
        output = ""
        for each_row in rows:
            output += each_row
        return output


# instanciate your Problem class and run
prob = Problem()
prob.run()
