"""
This program contains:
- a base class LeetCodeProblem with utilities for testing

- a basic linked list implementation and conversion utility
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