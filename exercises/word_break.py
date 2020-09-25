from base import LeetCodeProblem


class Problem(LeetCodeProblem):
    # for behaviours other than exact match between solution output and expected output
    # see # Testers in README.md
    """
    https://leetcode.com/problems/word-break/
    """
    def get_tests(self):
        # return test cases here
        return (
            # each test case has the following structure
            # ( parameter , expected output ),
            # # OR # #
            # ( (param1, param2), expected output ),
            (("leetcode", ["leet", "code"]), True),
            (("applepenapple", ["apple", "pen"]), True),
            (("catsandog", ["cats", "dog", "sand", "and", "cat"]), False),
            (("catsandox", ["cats", "ox", "and", "cat"]), True),
            (("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]), False),
        )

    def solution(self, s, wordDict):
        # have fun ~ ^_^
        # make a dict for caching function calls
        cache = {}
        # convert wordDict to set for quicker access
        words = set(wordDict)

        def cached(decoratee):
            def _inner(*args):
                try:
                    return cache[args]
                except KeyError:
                    result = decoratee(*args)
                    cache[args] = result
                    return result

            return _inner

        @cached
        def could_match(in_string):

            # base case, finished match on all chars
            if len(in_string) == 0:
                return True

            pointer = 1  # <= no need to check empty string
            while pointer < len(in_string) + 1:

                # current word found and rest of the string could be matched
                if in_string[:pointer] in words and could_match(in_string[pointer:]):
                    return True
                else:
                    pointer += 1

            # failed to match entire string
            return False

        return could_match(s)


# instanciate your Problem class and run
prob = Problem()
prob.run()
