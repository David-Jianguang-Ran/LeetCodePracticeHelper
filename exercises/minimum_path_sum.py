from base import LeetCodeProblem


class Problem(LeetCodeProblem):
    # for behaviours other than exact match between solution output and expected output
    # see # Testers in README.md
    """
    https://leetcode.com/problems/minimum-path-sum/

    i think we do tabulation here
    """
    def get_tests(self):
        # return test cases here
        return (
            # each test case has the following structure
            # ( parameter , expected output ),
            # # OR # #
            # ( (param1, param2), expected output ),
            ([
                 [1,3,1],
                 [1,5,1],
                 [4,2,1]
             ], 7),
            ([
                 [36, 49, 89, 75, 22, 37, 80, 5, 32, 89, 1, 50, 9, 28, 57, 14, 21, 46, 50, 15, 5, 97, 15, 26, 11, 32, 50, 14, 39, 22, 93, 55, 3, 7, 57, 90, 28, 66, 96, 30, 72, 17, 87, 19, 29, 31, 38, 27, 70, 7, 21, 67, 20, 100, 85, 92, 89, 94, 86, 25, 80, 3, 15, 86, 58, 56, 5, 82, 46, 62, 82, 26, 9, 41, 75, 89, 55, 19, 70, 64, 97, 57, 50, 4, 83, 41, 57, 11, 51, 78, 1, 46, 64, 11, 16, 5, 15, 21, 10, 32],
                 [42, 18, 62, 29, 15, 49, 16, 82, 42, 65, 93, 66, 16, 1, 76, 60, 53, 3, 85, 77, 68, 28, 55, 34, 2, 28, 11, 43, 25, 38, 33, 30, 54, 1, 68, 8, 38, 93, 33, 72, 66, 42, 69, 72, 45, 98, 13, 92, 56, 10, 73, 6, 58, 23, 56, 61, 3, 32, 83, 45, 23, 73, 98, 40, 42, 45, 81, 17, 53, 23, 9, 24, 19, 36, 67, 83, 40, 19, 17, 98, 63, 15, 97, 97, 15, 13, 16, 71, 86, 20, 61, 49, 55, 21, 34, 8, 68, 8, 32, 8],
                 [23, 40, 97, 51, 0, 93, 60, 46, 40, 33, 78, 83, 29, 95, 48, 80, 31, 73, 41, 29, 100, 54, 44, 30, 73, 84, 65, 94, 83, 84, 29, 31, 3, 24, 65, 49, 88, 37, 21, 65, 62, 31, 87, 51, 95, 6, 76, 1, 80, 56, 10, 27, 62, 8, 59, 11, 47, 65, 37, 78, 37, 64, 7, 99, 83, 27, 84, 82, 53, 57, 72, 86, 55, 10, 51, 96, 22, 38, 34, 55, 62, 89, 45, 54, 60, 76, 76, 48, 75, 56, 97, 91, 73, 9, 94, 87, 47, 68, 2, 53],
                 [18, 3, 10, 73, 95, 57, 86, 62, 0, 96, 43, 91, 49, 77, 73, 68, 97, 84, 74, 68, 3, 26, 14, 69, 58, 48, 13, 74, 24, 80, 14, 36, 10, 33, 75, 5, 74, 57, 26, 43, 49, 55, 53, 7, 80, 23, 12, 19, 79, 89, 66, 89,12, 51, 0, 25, 13, 44, 86, 29, 89, 85, 93, 62, 34, 27, 61, 58, 87, 71, 71, 46, 91, 30, 54, 47, 44, 88,98, 8, 96, 48, 15, 91, 49, 97, 92, 90, 92, 71, 44, 41, 36, 55, 68, 64, 95, 23, 7, 17],
                 [19, 7, 94, 42, 61, 72, 83, 76, 19, 59, 43, 40, 98, 16, 63, 30, 99, 2, 7, 88, 48, 94, 29, 24, 36, 44,71, 82, 57, 3, 99, 88, 63, 30, 63, 67, 33, 69, 80, 0, 97, 80, 85, 15, 97, 54, 18, 72, 85, 59, 58, 22,97, 50, 97, 91, 97, 96, 96, 38, 51, 56, 46, 49, 51, 67, 80, 57, 77, 60, 1, 9, 33, 81, 12, 23, 18, 68,95, 69, 27, 7, 2, 54, 9, 90, 1, 87, 55, 24, 26, 74, 85, 97, 21, 58, 13, 63, 24, 84]
             ], 4334),
        )

    def solution(self, grid):
        # have fun ~ ^_^
        grid_cache = [[None for i in range(len(grid[0]))] for j in range(len(grid))]

        def cached(decoratee):
            """ caches result and returns cache for later calls, pure functions only"""
            def _inner(x, y):
                c = grid_cache[x][y]

                if c is None:
                    r = decoratee(x, y)
                    grid_cache[x][y] = r
                    return r
                else:
                    return c

            return _inner

        @cached
        def shortest_path_to(x, y):

            # shortest path here is cost for here plus smallest next tile
            working_count = grid[x][y]

            if x < len(grid) - 1:
                below = shortest_path_to(x + 1, y)
            else:
                below = None

            if y < len(grid[0]) - 1:
                beside = shortest_path_to(x, y + 1)
            else:
                beside = None

            if below is not None and beside is not None:
                working_count += min(below, beside)
            elif below is not None:
                working_count += below
            elif beside is not None:
                working_count += beside
            else:
                # base case, reached the bottom right
                pass

            return working_count

        out = shortest_path_to(0,0)
        return out


# instanciate your Problem class and run
prob = Problem()
prob.run()
