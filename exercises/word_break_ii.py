from base import LeetCodeProblem


class Problem(LeetCodeProblem):
    # for behaviours other than exact match between solution output and expected output
    # see # Testers in README.md
    tester = "all"
    """
    https://leetcode.com/problems/word-break-ii/
    
    first approach too slow, let's make the recursive function more caching friendly
    
    """
    def get_tests(self):
        # return test cases here
        return (
            # each test case has the following structure
            # ( parameter , expected output ),
            # # OR # #
            # ( (param1, param2), expected output ),
            (("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]), ["pine apple pen apple","pineapple pen apple","pine applepen apple"]),
            (("catsanddog", ["cat", "cats", "and", "sand", "dog"]), ["cats and dog", "cat sand dog"]),
            (("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]), []),
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
        def find_match(to_match: str):
            """ this function returns a list of found complete sentence"""
            # base case, no more string to match
            if len(to_match) == 0:
                return True  # <= removing the last space inserted by prev function call

            # try matching dict word by increasing a window starting a beginning of to_match
            found_all = []
            for i in range(1, len(to_match) + 1):
                if to_match[:i] in words:
                    found = find_match(to_match[i:])
                    if found is True:
                        # reached end of string, start building output
                        found_all.append(to_match[:i])
                    elif isinstance(found, list):
                        # take all returned output string and add current word to it
                        found_all += [to_match[:i] + " " + each for each in found]
                    else:
                        TypeError(f"check return value ({found},) from find_match")

            return found_all

        all_found = find_match(s)

        return all_found


# instanciate your Problem class and run
prob = Problem()
prob.run()
