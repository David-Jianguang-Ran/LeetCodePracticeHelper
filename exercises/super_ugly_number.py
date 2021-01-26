from base import LeetCodeProblem


class Problem(LeetCodeProblem):
    # for behaviours other than exact match between solution output and expected output
    # see # Testers in README.md
    """
    https://leetcode.com/problems/super-ugly-number/

    # first attempt:
    ## invariant
    since all prime factor of SUNum are in primes,
    it means SUNums can be obtained by multiplying primes

    ## approach:
    generate SUNum by multiplying members of primes and push onto a max heap
    when max heap reaches n size, get max
    """
    def get_tests(self):
        # return test cases here
        return (
            # each test case has the following structure
            # ( parameter , expected output ),
            # # OR # #
            # ( (param1, param2), expected output ),
            ((12, [2, 7, 13, 19]), 32),
            ((80, [2,3,7,11,19,31,37,41,43,47]), 189),
            ((3, [2]), 4),
            ((10, [2,5,7,11,13,17,23,29,43,53]), 14),
            ((35, [2,5,7,11,13,23,29,31,53,67,71,73,79,89,97,107,113,127,131,137]), 67),
            ((80, [2,5,11,17,41,47,53,59,61,67,73,79,89,97,103,107,109,113,127,137]), 274),
            ((850, [7,13,29,31,37,41,43,53,59,61,71,73,79,83,89,101,107,109,127,131,137,149,151,157,173,227,229,233,239,257]), 48581),
            # ((100000, [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]), 1092889481),
        )

    def solution(self, n, primes):
        # have fun ~ ^_^

        class SuperUglyLineUp:
            """This is a max heap filled with unique values only"""
            def __init__(self):
                self.__array = [1]

            @property
            def count(self):
                return len(self.__array)

            @property
            def max(self):
                return self.__array[0]

            @property
            def second_max(self):
                return max(self.__array[1:3])

            def push(self, value: int):
                self.__array.append(value)
                self._max_heapify(self.count - 1)

            def pop(self):
                # swap root with a leaf and return leaf
                found_max = self.max
                self.__array[0] = self.__array[-1]
                self.__array.pop()
                self._max_heapify(0, down_heap=True)
                return found_max

            def pop_push(self, value: int):
                # pop max first, then push onto the first position, restore heap
                self.__array[0] = value
                self._max_heapify(0, down_heap=True)

            def _max_heapify(self,__index,down_heap=False):

                parent = self.__array[__index]
                left_i = __index * 2 + 1
                left_child = self.__array[left_i] if left_i < self.count else None
                right_child = self.__array[left_i + 1] if left_i + 1 < self.count else None
                swap_index = None

                if (left_child is not None and parent < left_child) or (right_child is not None and parent < right_child):
                    # heap property violated
                    # swap parent with biggest child

                    # the switch below is so long and repetitive
                    # TODO : find better way to resolve swap
                    if left_child is None:
                        swap_index = left_i + 1
                        swap_value = right_child
                    elif right_child is None:
                        swap_index = left_i
                        swap_value = left_child
                    # both children present, swap biggest
                    elif left_child > right_child:
                        swap_index = left_i
                        swap_value = left_child
                    else:
                        swap_index = left_i + 1
                        swap_value = right_child

                    # do the swap
                    self.__array[swap_index] = parent
                    self.__array[__index] = swap_value

                if down_heap and swap_index:
                    self._max_heapify(swap_index, down_heap=True)
                elif not down_heap and __index != 0:
                    self._max_heapify((__index - 1) // 2)

        def make_ugly_nums(__prev, __clip=0):
            """
            returns all possible product between __prev and primes
            TODO : needs a new way of generating ugly numbers
            """
            output = set()
            __min = None

            for __i, __each in enumerate(__prev):
                if __clip != 0:
                    to_multiply = primes[:-__clip]
                else:
                    to_multiply = primes

                for each_prime in to_multiply:
                    num = __each * each_prime
                    if __min is None or __min > num:
                        __min = num
                    output.add(num)
            return output, __min

        # first we make our queue
        queue = SuperUglyLineUp()
        to_append = primes
        smallest = 0
        max_clip = len(primes) // 4 * 3
        clip = 0
        break_next = False
        while True:
            # push known ugly nums to queue
            for each_ugly_num in to_append:
                if queue.count > n:
                    queue.pop_push(each_ugly_num)
                else:
                    queue.push(each_ugly_num)

            if smallest * primes[0] > queue.second_max and queue.count > n:
                break

            # stop recording ugly numbers when no new smaller number is generated
            to_append, smallest = make_ugly_nums(to_append, min(max_clip, clip))
            clip += len(primes) // 4

        # return second max
        return queue.second_max


# instanciate your Problem class and run
prob = Problem()
prob.run()
