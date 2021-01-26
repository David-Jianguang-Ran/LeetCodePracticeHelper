from base import LeetCodeProblem


class Problem(LeetCodeProblem):
    # for behaviours other than exact match between solution output and expected output
    # see # Testers in README.md
    """
    https://leetcode.com/problems/unique-binary-search-trees/

    wow this is such a good but hard problem,
    i got as far trying to define the output recursively before i had to look it up

    turns out catalan numbers are a thing! haha
    """
    def get_tests(self):
        # return test cases here
        return (
            # each test case has the following structure
            # ( parameter , expected output ),
            # # OR # #
            # ( (param1, param2), expected output ),
            (2, 2),
            (3, 5),
            (4, 14),
            (5, 42),
            (6, 132),
            (7, 429)
        )

    def solution(self, n):
        # formula for catalan number n
        # Cn = (n * 2)! / (n+1)!n!

        top = 1
        for i in range(n + 2, n * 2 + 1):
            top = top * i

        bottom = 1
        for i in range(1, n + 1):
            bottom = bottom * i

        return top // bottom


# instanciate your Problem class and run
prob = Problem()
prob.run()
