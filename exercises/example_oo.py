from base import LeetCodeProblem


class Problem(LeetCodeProblem):
    # for behaviours other than exact match between solution output and expected output
    # see # Testers in README.md
    tester = "object"
    """
    https://leetcode.com/problems/kth-largest-element-in-a-stream/
    
    """
    def get_tests(self):
        # return test cases here
        return (
            # this tester requires specific test case structure:
            # `( (init_args,), [(method_name, *args,)], [results] ) `
            # note that expected must be a list, not a tuple
            ((3, [4,5,8,2]), [[("add", 3), ("add", 5),("add", 10),("add", 9),("add", 4),], [4,5,5,8,8]]),
            ((3, [4, 5, 8, 2, 5]), [[("add", 3), ("add", 5), ("add", 10), ("add", 9), ("add", 4), ], [5, 5, 5, 8, 8]]),

        )

    def solution(self, *args):
        # initialize a instance of your class here
        return KthLargest(*args)


class KthLargest:
    """ this is a min heap based approach"""
    def __init__(self, k, nums):
        self._array = nums.copy()
        self.k = k

        # restore heap property from leaves up
        for i in range(len(nums)):
            self.min_heapify(len(nums) - 1 - i)

    def min_heapify(self, start_at, down_heap=True):

        left_child = start_at * 2 + 1 if start_at * 2 + 1 < len(self._array) else None
        right_child = start_at * 2 + 2 if start_at * 2 + 2 < len(self._array) else None

        swap_i = None
        swap_val = None

        if left_child is None and right_child is None:
            # leaf node, trivially min heap
            return
        elif left_child is not None and self._array[start_at] > self._array[left_child] \
                or\
                right_child is not None and self._array[start_at] > self._array[right_child]:
            # heap property violated, do the swap with min value of left and right,
            # or just the one that exists
            if right_child is not None and self._array[right_child] < self._array[left_child]:
                swap_i = right_child
                swap_val = self._array[right_child]
            else:
                swap_i = left_child
                swap_val = self._array[left_child]

            # do the swap
            self._array[swap_i] = self._array[start_at]
            self._array[start_at] = swap_val
        else:
            # heap property satisfied
            return

        # recursion
        if down_heap:
            self.min_heapify(swap_i)
        elif start_at != 0:
            # if not root already, go up heap, start at parent
            self.min_heapify((start_at - 1) // 2, down_heap=False)

    @property
    def min(self):
        return self._array[0]

    def extract_min(self):
        # to extract min,
        # we pop min then move end element to front
        min_val = self._array[0]
        self._array[0] = self._array[-1]
        self._array = self._array[:-1]

        # restore heap property from root down
        self.min_heapify(0)

        return min_val

    def add(self, num):

        # first add new num as a leaf
        self._array.append(num)
        # restore heap property
        if len(self._array) < 4:
            self.min_heapify(0)
        else:
            self.min_heapify((len(self._array) - 2) // 2, down_heap=False)

        # pop min untill heap only has k item
        while len(self._array) > self.k:
            self.extract_min()

        return self.min


# instanciate your Problem class and run
prob = Problem()
prob.run()
