from base import LeetCodeProblem


class Problem(LeetCodeProblem):
    # for behaviours other than exact match between solution output and expected output
    # see # Testers in README.md
    """"""
    def get_tests(self):
        # return test cases here
        return (
            # each test case has the following structure
            # ( parameter , expected output ),
            # # OR # #
            # ( (param1, param2), expected output ),
            (),
        )

    def solution(self, *args):
        # have fun ~ ^_^
        return


# instanciate your Problem class and run
prob = Problem()
prob.run()
