"""
This program contains:
**in this file**
- a base class LeetCodeProblem with utilities for testing
**in utils**
- a basic linked list implementation and conversion utility
- a function call caching decorator (obviously pure functions only)
- a python implementation of min heap
"""
import time


##
# Result tester decorator
def make_tester(store: dict, key: str = None):
    """this function saves the decoratee under key to dict store"""
    def _decorator(decoratee):
        if key is None:
            name = decoratee.__name__
        else:
            name = key

        store[name] = decoratee
        return decoratee

    return _decorator


class LeetCodeProblem:
    _testers = {}

    def __init__(self):
        self.error_cases = []
        self.error_count = 0
        self.total_count = 0
        self.time_elapsed = None

    def get_tests(self) -> (()):
        """
        # returns a tuple of test cases
        # each test case has the following structure
        # ( parameter , expected output ),
        # # OR # #
        # ( (param1, param2), expected output ),
        """
        raise NotImplementedError

    def solution(self, *args):
        """
        step-by-step user guide:
        >>see example.py for code example<<

        1. inherent from this LeetCodeProblem class
        2. override get_tests to return a tuple of test cases
        3. override solution function with the body of your solution
        4. make a new instance of your class and call instance.run()
        5. (optional) instance.print_result can be called repeatedly, this can be useful in ipython (maybe)
        """
        raise NotImplementedError

    def print_result(self):
        print(f"did {self.total_count} tests, {self.error_count} fails, time spent {self.time_elapsed :.2f} ms")
        if self.error_count:
            print("Input | Expected | Output")
            print(*[f"{each_case} \n" for each_case in self.error_cases])

    def run(self, verbose=False):
        start_time = time.time()
        for each_case in self.get_tests():
            self.total_count += 1
            params, expected = each_case

            if verbose:
                print("______________")
                print(f"input : {params}")

            # call the solution and obtain results
            try:
                if isinstance(params, tuple):
                    result = self.solution(*params)
                else:
                    result = self.solution(params)
            except RuntimeError:
                self.error_count += 1
                self.error_cases.append((params, expected, None))
                continue

            # run tester function and obtain stats
            try:
                try:
                    # resolve tester
                    __tester = self._testers[self._get_tester()]
                    __tester(self, expected, result)
                except KeyError:
                    print(f"Invalid mode <{self.tester}> specified, printing results for manual inspection \n ______________")
                    print(expected, result)
                    self.error_count += 1
            except AssertionError:
                self.error_count += 1
                self.error_cases.append((params, expected, result))

        self.time_elapsed = (time.time() - start_time) * 1000

        # final printout
        self.print_result()

    ##
    # Testers

    # To alter the default behaviour,
    # set self.tester to the key of a tester function decorated with @bind_to

    def _get_tester(self):

        try:
            return self.tester
        except AttributeError:
            return "exact"

    @make_tester(_testers, key="exact")
    def exact_match(self, truth, result):
        assert truth == result

    @make_tester(_testers, key="any")
    def one_to_many(self, truth, result):
        if not isinstance(result, (list, tuple)):
            raise TypeError("expected output must be a list or tuple")
        assert result in truth

    @make_tester(_testers, key="all")
    def many_to_many(self, truth, result):
        if not isinstance(result, (list, tuple)):
            raise TypeError("expected output must be a list or tuple")
        assert sorted(truth) == sorted(result)

    @make_tester(_testers, key="linked_lists")
    def linked_lists_equal(self, truth_head, result_head):

        if not isinstance(truth_head, ListNode) or not isinstance(result_head, ListNode):
            raise TypeError("linked list comparison can only take ListNode as arguments")

        # iterate through both at the same time and compare
        left = truth_head
        right = result_head
        while left is not None or right is not None:

            if left is None or right is None:
                raise AssertionError
            else:
                assert left.val == right.val

                if left:
                    left = left.next

                if right:
                    right = right.next

    @make_tester(_testers, key="object")
    def method_calls(self, expected: list, instance):
        """
        in order to use this tester the solution must
        1. take arguments for yourclass.init
        2. return instance of your class

        this tester requires specific test case structure:
        `( (init_args, ) , [(method_name, *args,)], [results] ) `
        note that expected must be a list, not a tuple
        its sort of a hacky mess i know (:P)
        """
        calls, expected_results = expected

        # call each method specified and collect results in a list
        working_results = [getattr(instance, each_call[0])(*each_call[1:]) for each_call in calls]

        # this is a hideous hack !
        # modifying expected to pass error data back
        if working_results != expected_results:
            expected[1] = working_results
            expected[0] = expected_results
            raise AssertionError


##
# linked list utility
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode:{self.val}"


def to_linked_list(plist):
    """takes python list and return head of linked list"""
    if len(plist) == 0:
        return None

    head = ListNode(plist[0])
    tail = head

    for val in plist[1:]:
        current = ListNode(val)
        tail.next = current
        tail = current

    return head


def to_plist(head):
    """scans from head onwards, returns python list"""
    plist = [head.val]
    current = head

    while current.next:
        plist.append(current.next.val)
        current = current.next

    return plist


##
# Caching utility
def cached(__cache: dict):
    """
    cache returned values in __cache,
    note that decoratee function can *ONLY* take positional args
    """
    def _decorator(decoratee):

        def _inner(*args):
            try:
                return __cache[args]
            except KeyError:
                result = decoratee(*args)
                __cache[args] = result
                return result

        return _inner

    return _decorator


##
# heap utility
class MinHeap:
    def __init__(self, initial_array=None, known_heap=False):
        if initial_array is None:
            self.__array = []
        else:
            self.__array = initial_array.copy()

            if not known_heap:
                # build heap property from leaves up
                for i in range(len(initial_array)):
                    self._min_heapify(len(initial_array) - 1 - i, down_heap=True)

    def __len__(self):
        return len(self.__array)

    def min(self):
        return self.__array[0]

    def pop_min(self):
        value = self.__array[0]
        # pop end element and replace root, then restore heap property from root down
        self.__array[0] = self.__array.pop()
        self._min_heapify(0, down_heap=True)
        return value

    def push(self, value):
        self.__array.append(value)
        self._min_heapify(len(self.__array) - 1)

    def _min_heapify(self, __index, down_heap=False):
        parent = self.__array[__index]
        left_i = __index * 2 + 1
        left_child = self.__array[left_i] if left_i < self.__len__() else None
        right_child = self.__array[left_i + 1] if left_i + 1 < self.__len__() else None
        swap_index = None

        if (left_child is not None and parent > left_child) or (right_child is not None and parent > right_child):
            # heap property violated
            # swap parent with smallest child

            # the switch below is so long and repetitive
            # TODO : find better way to resolve swap
            if left_child is None:
                swap_index = left_i + 1
                swap_value = right_child
            elif right_child is None:
                swap_index = left_i
                swap_value = left_child
            # both children present, swap biggest
            elif left_child < right_child:
                swap_index = left_i
                swap_value = left_child
            else:
                swap_index = left_i + 1
                swap_value = right_child

            # do the swap
            self.__array[swap_index] = parent
            self.__array[__index] = swap_value

        if down_heap and swap_index:
            self._min_heapify(swap_index, down_heap=True)
        elif not down_heap and __index != 0:
            self._min_heapify((__index - 1) // 2)


if __name__ == "__main__":
    print("""
    step-by-step user guide:
    >>see example.py for code example<<

    1. inherent from this LeetCodeProblem class
    2. override get_tests to return a tuple of test cases
    3. override solution function with the body of your solution
    4. make a new instance of your class and call instance.run()
    5. (optional) instance.print_result can be called repeatedly, this can be useful in ipython (maybe)
    """
    )
