from base import LeetCodeProblem


class Problem(LeetCodeProblem):
    # for behaviours other than exact match between solution output and expected output
    # see # Testers in README.md
    """
    https://leetcode.com/problems/simplify-path/

    i guess for this one we do a split string?

    then walk through each
    """
    def get_tests(self):
        # return test cases here
        return (
            # each test case has the following structure
            # ( parameter , expected output ),
            # # OR # #
            # ( (param1, param2), expected output ),
            ("/home/", "/home"),
            ("/../", "/"),
            ("/home//foo/", "/home/foo"),
            ("/a/./b/../../c/", "/c"),
            ("//leetcode.com/problems/simplify_path/d/e/s/../../g","/leetcode.com/problems/simplify_path/d/g")
        )

    def solution(self, path: str) -> str:
        # have fun ~ ^_^
        if not path[0] == "/":
            raise ValueError

        # split path into steps
        # take each step
        steps_to_take = path.split("/")
        steps_taken = []
        for each in steps_to_take:
            if each == "" or each == ".":
                # no op?
                continue
            elif each == "..":
                if len(steps_taken) > 0:
                    steps_taken.pop()
            else:
                # normal dir, append to path
                steps_taken.append(each)

        # convert to output format
        out_string = "/"
        for each in steps_taken:
            if out_string[-1] == "/":
                out_string += each
            else:
                out_string += "/" + each

        return out_string


# instanciate your Problem class and run
prob = Problem()
prob.run()