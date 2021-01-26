from base import LeetCodeProblem


class Problem(LeetCodeProblem):
    # for behaviours other than exact match between solution output and expected output
    # see # Testers in README.md
    """
    https://leetcode.com/problems/decode-ways/

    """
    def get_tests(self):
        # return test cases here
        return (
            # each test case has the following structure
            # ( parameter , expected output ),
            # # OR # #
            # ( (param1, param2), expected output ),
            ("1291255983", 6),
            ("000122242", 0),
            ("202", 1),
            ("12", 2),
            ("226", 3),
            ("0", 0),
            ("1", 1),
            ("2", 1),

        )

    def solution(self, s):
        # have fun ~ ^_^
        cache = {}

        def cached(decoratee):
            def _inner(*args):
                try:
                    return cache[args]
                except KeyError:
                    result = decoratee(*args)
                    cache[args] = result
                    return result

            return _inner


        def find_ways(__string):
            # if matching is finished or only one char left, then we've found a way
            if len(__string) == 0:
                return 1
            elif len(__string) == 1:
                return 1 if __string != "0" else 0

            # how many children situ depends on the first two digits here
            d1 = int(__string[0])
            if d1 == 1:
                return find_ways(__string[1:]) + find_ways(__string[2:])
            elif d1 == 2 and int(__string[1]) <= 6:
                return find_ways(__string[1:]) + find_ways(__string[2:])
            elif d1 == 0:
                return 0
            else:
                return find_ways(__string[1:])

        result = find_ways(s)
        return result


# instanciate your Problem class and run
prob = Problem()
prob.run()
