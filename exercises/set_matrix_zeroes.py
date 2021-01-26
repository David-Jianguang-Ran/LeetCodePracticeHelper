from base import LeetCodeProblem


class Problem(LeetCodeProblem):
    # for behaviours other than exact match between solution output and expected output
    # see # Testers in README.md
    """
    https://leetcode.com/problems/set-matrix-zeroes/

    the problems hints toward a constant space solution,
    likely to be just looping through
    """
    def get_tests(self):
        # return test cases here
        return (
            # each test case has the following structure
            # ( parameter , expected output ),
            # # OR # #
            # ( (param1, param2), expected output ),
            (
                [
                    [1,1,1],
                    [1,0,1],
                    [1,1,1]
                ],
                [
                    [1,0,1],
                    [0,0,0],
                    [1,0,1]
                ]
            ),
        )

    def solution(self, matrix):
        # have fun ~ ^_^
        return


# instanciate your Problem class and run
prob = Problem()
prob.run()
