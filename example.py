from base import LeetCodeProblem, make_tester


class Problem(LeetCodeProblem):
    tester = "exact"  # <= this doesn't need to be stated explicitly for exact match
    # for behaviours other than exact match between solution output and expected output
    # see # Testers in README.md
    """
    url: https://leetcode.com/problems/unique-paths/
    """
    def get_tests(self):
        return (
            # each test case has the following structure
            # ( parameter , expected output ),
            # # OR # #
            # ( (param1, param2), expected output ),
            ((3, 2), 3),
            ((6, 8), 792),
            ((10, 10), 48620),
            ((50, 50), 25477612258980856902730428600),
            ((100, 100), 22750883079422934966181954039568885395604168260154104734000),
        )

    def solution(self, m, n):
        # main body of the solution
        memo = {}

        def cached(decoratee):
            """this caches the results, pure functions only, no methods allowed!"""
            def _inner(x, y):
                try:
                    return memo[(x, y)]
                except KeyError:
                    result = decoratee(x, y)
                    memo[(x, y)] = result
                    return result

            return _inner

        @cached
        def total_paths_to(x, y):
            # the number of paths to each location is sum of all immediately reachable locations
            total_here = 0

            # base case
            if x == m - 1 and y == n - 1:
                return 1

            # tally valid paths
            if x < m - 1:
                total_here += total_paths_to(x + 1, y)
            if y < n - 1:
                total_here += total_paths_to(x, y + 1)

            return total_here

        return total_paths_to(0, 0)

prob = Problem()
prob.run()
