from base import LeetCodeProblem

import random

class Problem(LeetCodeProblem):
    # for behaviours other than exact match between solution output and expected output
    # see # Testers in README.md
    tester = "all"
    """
    https://leetcode.com/problems/subsets-ii/

    use incrementing binary number to make a selector then into a set of immutable sets
    """
    def get_tests(self):
        # return test cases here
        return (
            # each test case has the following structure
            # ( parameter , expected output ),
            # # OR # #
            # ( (param1, param2), expected output ),
            (
                [1, 2, 2],
                [
                    [1],
                    [2],
                    [1,2,2],
                    [2,2],
                    [1,2],
                    []
                ]
            ),
            (
                [1,2,2,1],
                [[1, 2], [1, 1, 2, 2], [1], [1, 2, 2], [2], [1, 1, 2], [], [2, 2], [1, 1]]
            ),
            (
                [random.randint(1,64) for i in range(50)],[]
            )
        )

    def solution(self, nums):
        # have fun ~ ^_^
        subsets = set()

        # binary number based selector
        # i.e. '101' means selecting first and third element
        for i in range(int("".join(["1" for i in range(len(nums))]),2) + 1):
            # do selection
            working_set = []
            for index, selected in enumerate(f"{i:0{len(nums)}b}"):
                if int(selected):
                    working_set.append(nums[index])

            # append to record
            subsets.add(tuple(sorted(working_set)))

        return [list(each) for each in subsets]

# instanciate your Problem class and run
prob = Problem()
prob.run()
