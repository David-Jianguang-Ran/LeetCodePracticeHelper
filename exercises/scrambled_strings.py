from base import LeetCodeProblem


class Problem(LeetCodeProblem):
    # for behaviours other than exact match between solution output and expected output
    # see # Testers in README.md
    """
    scrambled strings yum!
    let's do that with some veggies (trees)

    so the approach is to keep track all permutations via a binary tree <= why binary? luck i guess
    each node at level d keep track of the dth char in permutation string

    the permutations binary tree could be built via a sliding window algorithm <= this is the clever bit
    each position could only have one of three possible values in a sliding window width 3 over original text,
    by ruling out text char already used, one can narrow down what this char could be,
    this insight in the core of the fast tree construction algorithm

    solutions are checked against the tree char/node by node
    """
    def get_tests(self):
        # return test cases here
        return (
            # each test case has the following structure
            # ( parameter , expected output ),
            # # OR # #
            # ( (param1, param2), expected output ),
            (("a", "a"), True),
            (("abcde", "baced"), True),
            (("abcde", "caebd"), False),
            (("abcdeb", "bacedb"), True),
            (("greate", "rgeate"), True),
            (("naranjaBaga", "narnajaaBga"), True),
            (("abcdefg", "aefgbcd"), True),  # <= looks like I misunderstood the spec completely
        )

    def solution(self, s1, s2):
        # have fun ~ ^_^
        # special case
        if len(s1) < 3:
            if s1 == s2 or s1[::-1] == s2:
                return True
            else:
                return False

        # first tree utilities
        def build_tree_with(current_leaves:[PermNode], char_window:str) -> [PermNode]:
            new_leaves = []
            for old_leaf in current_leaves:
                possible_chars = list(char_window)

                if len(possible_chars) == 3 and possible_chars[1] == old_leaf.value:
                    # when leaf node equals the middle of the range, only first of range can be child
                    new_leaf = old_leaf.create_children(possible_chars[0])
                    new_leaves.append(new_leaf)
                    continue
                elif old_leaf.value not in possible_chars:
                    # two situ
                    # old leaf is root => append both possible chars
                    # first of range is parent of old leaf, select the latter two in range
                    possible_chars = possible_chars[-2:]
                else:
                    # remove impossible case
                    possible_chars.remove(old_leaf.value)

                # append new leaf to old_leaf <= old leaf
                for each_char in possible_chars:
                    new_leaf = old_leaf.create_children(each_char)
                    new_leaves.append(new_leaf)

            return new_leaves

        def check_against_tree(_node: PermNode, check_str: str):
            if _node.is_leaf and len(check_str) == 0:
                return True
            elif check_str[0] in _node.children_vals:
                return check_against_tree(_node.children[check_str[0]], check_str[1:])
            else:
                return False

        # do sliding window
        root = PermNode()
        pointer = 2
        leaves = [root]
        while pointer <= len(s1) + 1:
            leaves = build_tree_with(leaves, s1[max(pointer - 3, 0): pointer])
            pointer += 1

        # check s2 against perm tree
        result = check_against_tree(root, s2)

        return result


class PermNode:
    def __init__(self, parent=None, value=None):
        self.value = value
        self.parent = parent
        self.children = {}

    def __repr__(self):
        return f"<Node:({self.value}) Children:{self.children_vals}>"

    @property
    def is_root(self):
        return self.parent is None

    @property
    def is_leaf(self):
        return self.children.__len__() == 0

    @property
    def children_vals(self):
        return list(self.children.keys())

    def create_children(self, value):
        """ creates node of value and attach to self and returns created node"""
        child = PermNode(self,value)
        self.children[value] = child
        return child











# instanciate your Problem class and run
prob = Problem()
prob.run()
