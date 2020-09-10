# LeetCode Practice Helper

A simple python program for running tests on algorithm challenge solutions.


## Guide:

#### Install
No installation necessary, just import objects from base.py into your python file.

#### Setting Up and Running a Problem
Subclass base.LeetCodeProblem class to use the library.  
A template.py is provided, simply copy and rename from template is usually all you'll need.   
See examples.py for details.  

#### Testers
Tester functions govern how output of a solution is checked against the expected case.  
select tester by setting YourClass.tester to a key value below, either as class variable or instance variable
Here are some available testers:  
- "exact" : output must exactly matches expected  
- "any" : output must match one element in expected, expected must be a list or tuple  
- "all" : output must have same elements as expected, expected must be a list or tuple  
- "linked_lists" : output must have same val element-wise as expected, both output and expected needs to be head ListNode    

You can also expand on the library by implementing your own testers and selecting it.  
Here is an example:
```python
from base import LeetCodeProblem, make_tester

class YourClass(LeetCodeProblem):
    # select your tester by key
    tester = "all"    
    
    # define your tester here
    @make_tester(LeetCodeProblem.__testers, key="all")
    def many_to_many(self, truth, result):
        if not isinstance(result, (list, tuple)):
            raise TypeError("expected output must be a list or tuple")
        assert sorted(truth) == sorted(result)
```

#### Bonus: Linked Lists Utility
This library also includes utility function for converting python lists to linked lists. Enjoy!  

__base.to_linked_list__ (plist : list) -> ListNode: 
"""takes python list and return head of linked list"""  

__base.to_plist__ (head : ListNode) -> list: 
"""scans from head onwards, returns python list"""
