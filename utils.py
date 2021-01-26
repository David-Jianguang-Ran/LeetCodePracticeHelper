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

