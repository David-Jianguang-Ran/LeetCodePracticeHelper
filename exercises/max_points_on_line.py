from base import LeetCodeProblem


class Problem(LeetCodeProblem):
    # for behaviours other than exact match between solution output and expected output
    # see # Testers in README.md
    """
    https://leetcode.com/problems/max-points-on-a-line/

    only 15% acceptance!! wow
    """
    def get_tests(self):
        # return test cases here
        return (
            # each test case has the following structure
            # ( parameter , expected output ),
            # # OR # #
            # ( (param1, param2), expected output ),
            ([[0,0],[1,1],[0,0]], 3),
            ([[0, 0], [1, 0]], 2),
            ([[0, 1], [0, 0]], 2),
            ([[-4, 1], [-7, 7], [-1, 5], [9, -25]], 3),
            ([], 0),
            ([[0, 0]], 1),
            ([[0, 0], [0, 0], [1,1]], 3),
            ([[0, 0], [0, 0]], 2),
            ([[1,1], [2,2], [3,3]], 3),
            ([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], 4),
            ([[1,9],[8,2],[3,3],[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], 4),
            ([[1, 9], [3, 0], [3, 3], [1, 1], [3, 2], [3, 7], [4, 1], [2, 3], [3, 4]], 5),

        )

    def solution(self, points):
        # have fun ~ ^_^
        max_found = 0

        def get_slope(a, b):
            if a[0] == b[0]:
                return "x"
            elif a[1] == b[1]:
                return "y"
            else:
                return f"{(a[0] - b[0]) / (a[1] - b[1]):.10}"

        def check_point(__point):
            """ returns max found and all lines that belong on max line"""
            hits = {"any":[]}
            for each_point in points:
                if each_point == __point:
                    hits["any"].append(each_point)
                else:
                    slope = get_slope(__point, each_point)
                    try:
                        hits[slope].append(each_point)
                    except KeyError:
                        hits[slope] = [each_point]

            # calculate max length
            max_length = 0
            max_val = []
            for key, val in hits.items():
                if len(val) > max_length and key != "any":
                    max_length = len(val)
                    max_val = val

            if len(hits) != 1:
                return max_val + hits["any"]
            else:
                return hits["any"]

        # main
        # we get a set of points to visit,
        # every check, remove visited AND max line members to save time
        to_visit = points.copy()
        max_line_count = 0
        while len(to_visit) > 0:
            visit_next = to_visit.pop()
            max_line_members = check_point(visit_next)

            # record max line
            if len(max_line_members) > max_line_count:
                max_line_count = len(max_line_members)

            # remove max line members from to_visit
            to_visit = [each for each in to_visit if each not in max_line_members]

        return max_line_count


# instanciate your Problem class and run
prob = Problem()
prob.run()
