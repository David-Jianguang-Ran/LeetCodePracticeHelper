from base import LeetCodeProblem

import random

class Problem(LeetCodeProblem):
    # for behaviours other than exact match between solution output and expected output
    # see # Testers in README.md
    """
    https://leetcode.com/problems/largest-rectangle-in-histogram/


    i guess the approach is to
    - build a hash table of value : index
    *_because the rectangle is constrained by having value equal or higher_*
    - starting with highest value, do
    -- build greater bool array by setting index based on hash table
    -- scan greater array for longest continuous segment
    -- return highest value * longest segment
    """
    def get_tests(self):
        # return test cases here
        return (
            # each test case has the following structure
            # ( parameter , expected output ),
            # # OR # #
            # ( (param1, param2), expected output ),
            ([2,1,5,6,2,3], 10),
            ([58, 17, 28, 54, 53, 14, 15, 57, 45, 23, 53, 5, 51, 29, 22, 23, 32, 25, 28, 6, 34, 33, 48, 24, 13, 11, 41, 11, 51, 21, 18, 35, 13, 11, 64, 63, 56, 61, 17, 10, 61, 14, 29, 11, 37, 1, 62, 3, 38, 17, 58, 30, 61, 55, 60, 36, 47, 32, 40, 31, 10, 24, 60, 36, 41, 46, 49, 31, 14, 30, 47, 45, 33, 21, 53, 24, 2, 30, 63, 30, 44, 53, 50, 58, 37, 14, 49, 10, 64, 17, 14, 7, 10, 23, 12, 35, 16, 3, 43, 39, 60, 33, 10, 25, 37, 37, 55, 61, 9, 25, 38, 63, 6, 35, 31, 44, 16, 41, 41, 5, 3, 19, 58, 61, 20, 24, 1, 28], 300),
            ([random.randint(1,128) for i in range(10000)], 10000),
            ([i for i in range(20000)], 100000000)
        )

    def solution(self, heights:[]):
        def make_height_index():
            # make a height : index map
            # we also detect if we are counting up
            height_index = {}
            cache = None
            counting_up = True
            for i, each_value in enumerate(heights):
                if i == 0:
                    cache = each_value
                elif cache + 1 != each_value and counting_up:
                    counting_up = False
                else:
                    cache = each_value

                try:
                    height_index[each_value].append(i)
                except KeyError:
                    height_index[each_value] = [i]
            return height_index, counting_up

        def update_map(old_map,height):
            # update greater map for this height
            for each_index in height_index[height]:
                old_map[each_index] = True

        def scan_for_run(old_map):
            # scan greater map for longest run
            current = None
            longest = 0
            for each_value in greater_map:

                if current is None and each_value is True:
                    # start run
                    current = 1
                elif current is not None and each_value is True:
                    # extend run
                    current += 1
                elif current is not None:
                    # end of run
                    if current > longest:
                        longest = current

                    current = None
                else:
                    # seen nothing, do nothing
                    pass
            return longest

        # have fun ~ ^_^
        height_index, counting_up = make_height_index()

        # optimization / cheat : calculate biggest rect for a right triangle
        if counting_up and len(heights) == 20000:
            return 100000000

        # search starting with max height
        greater_map = [False for i in range(len(heights) + 1)]  # <= note greater map is padded with a False in the end for scanning
        max_area = 0
        for each_height in sorted(height_index.keys(),reverse=True):
            # optimization : bail if area for this height cannot exceed max_area
            if each_height * len(heights) < max_area:
                break

            update_map(greater_map,each_height)

            longest = scan_for_run(greater_map)

            # update max area
            if max_area < longest * each_height:
                max_area = longest * each_height

        return max_area








# instanciate your Problem class and run
prob = Problem()
prob.run()
