from base import LeetCodeProblem


class Problem(LeetCodeProblem):
    # for behaviours other than exact match between solution output and expected output
    # see # Testers in README.md
    tester = "all"
    """
    https://leetcode.com/problems/permutations/
    
    i can search recursively or i can just write out numbers in blocks
    seems like the blocks thing doesnt generalize to n > 3
    
    """
    def get_tests(self):
        # return test cases here
        return (
            # each test case has the following structure
            # ( parameter , expected output ),
            # # OR # #
            # ( (param1, param2), expected output ),
            ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
            ( [1,2,3], [[1,2,3], [1,3,2], [2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
            ([0,1], [[0,1],[1,0]]),
            ([0,1,2,3,4,5,6,7,8], [])  # <= too many permutation to keep track of

        )

    def solution(self, nums):
        # have fun ~ ^_^
        results = {}
        def cache_results(decoratee):
            def inner(options):
                try:
                    return results[options]
                except KeyError:
                    results[options] = decoratee(options)
                    return results[options]

            return inner

        @cache_results
        def find_perm(options:tuple):
            # base case, found the end of perm
            if len(options) == 0:
                return [[]]
            else:
                found_perms = []
                for i, item in enumerate(options):
                    # remove item and pass on
                    next_options = options[:i] + options[i+1:]
                    next_result = find_perm(next_options)

                    for each_perm in next_result:
                        found_perms.append([item] + each_perm)

                return found_perms

        all_results = find_perm(tuple(nums))

        return all_results


# instanciate your Problem class and run
prob = Problem()
prob.run()
