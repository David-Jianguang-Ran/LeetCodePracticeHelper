from base import LeetCodeProblem


class DataNode:
    """min heap node with incrementing priority"""
    serial = 0

    def __init__(self, key, value, priority=None,position=None):
        # data
        self.key = key
        self.val = value
        if not priority:
            priority = self.ticker()
        self.priority = priority
        self.position = position

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.priority == other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __repr__(self):
        return f"<DataNode:k={self.key}pri={self.priority}pos={self.position}>"

    @classmethod
    def ticker(cls):
        cls.serial += 1
        return cls.serial


class LRUCache:
    """
    data is kept as a custom node obj, accessible by both hash table and heap
    LRU is tracked via a min heap
    """
    def __init__(self, capacity: int):
        self.capacity = capacity

        self._by_key = {}
        self._by_pos = {}

    def put(self, key, value):
        if key in self._by_key:
            # get data node instance
            instance = self._by_key[key]

            # update instance
            instance.val = value

            # update usage
            instance.priority = instance.ticker()
            self._min_heapify(instance.position)
        else:
            if len(self._by_pos) < self.capacity:
                # make node
                pos = f"{len(self._by_pos) + 1:b}"
                new_node = DataNode(key,value,position=pos)
                # append to record
                self._by_key[key] = new_node
                self._by_pos[pos] = new_node
                # restore heap up
                self._min_heapify(pos,down_heap=False)
            else:
                # pop and replace
                self._replace_min(key,value)

    def get(self,key):
        if key in self._by_key:
            # get data node instance
            instance = self._by_key[key]

            # update usage
            instance.priority = instance.ticker()
            self._min_heapify(instance.position)

            return instance.val

        else:
            return -1

    def _min_heapify(self, position: str, down_heap=True):
        """this always goes down heap"""
        # compute node pri, key
        parent = self._by_pos[position]

        try:
            left_child = self._by_pos[position + "0"]
        except KeyError:
            left_child = None

        try:
            right_child = self._by_pos[position + "1"]
        except KeyError:
            right_child = None

        # check and restore heap property
        if (left_child is not None and parent > left_child) or (
                right_child is not None and parent > right_child):
            # heap property violated
            # swap parent with smallest child

            # the switch below is so long and repetitive
            # TODO : find better way to resolve swap
            if left_child is None:
                to_swap = right_child
            elif right_child is None:
                to_swap = left_child
            elif left_child > right_child:
                to_swap = right_child
            else:
                to_swap = left_child

            # do the swap
            p_pos = parent.position
            swap_pos = to_swap.position

            parent.position = swap_pos
            to_swap.position = p_pos

            self._by_pos[swap_pos] = parent
            self._by_pos[p_pos] = to_swap

            if down_heap:
                # continue down heap
                self._min_heapify(swap_pos)
            elif not down_heap and parent.position != "1":
                # continue up heap if not root
                self._min_heapify(parent.position[:-1])

    def _replace_min(self,new_key, new_val):

        new_node = DataNode(new_key,new_val,position="1")

        # pop old min
        self._by_key.pop(self._by_pos["1"].key)
        # record new node
        self._by_key[new_key] = new_node
        self._by_pos["1"] = new_node
        # restore down heap
        self._min_heapify("1")


class Problem(LeetCodeProblem):
    # for behaviours other than exact match between solution output and expected output
    # see # Testers in README.md
    """
    https://leetcode.com/problems/lru-cache/
    """
    tester = "object"
    def get_tests(self):
        # return test cases here
        return (
            # each test case has the following structure
            # ( parameter , expected output ),
            # # OR # #
            # ( (param1, param2), expected output ),
            (
                2,[
                [
                    ("put",1,1),
                    ("put",2,2),
                    ("get",1),
                    ("put",3,3),
                    ("get",2),
                    ("put",4,4),
                    ("get",1),
                    ("get",3),
                    ("get",4)
                ],
                [
                    None,
                    None,
                    1,
                    None,
                    -1,
                    None,
                    -1,
                    3,
                    4
                ]]
            ),
        )

    def solution(self, capacity):
        # have fun ~ ^_^
        return LRUCache(capacity)


# instanciate your Problem class and run
prob = Problem()
prob.run()
