# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        firstNumber = []
        secondNumber = []
        
        p1 = l1
        p2 = l2
        
        while p1 is not None:
            firstNumber.insert(0, p1.val)
            p1 = p1.next
            
        while p2 is not None:
            secondNumber.insert(0, p2.val)
            p2 = p2.next
            
        firstNumberCombined =  int( ''.join(str(e) for e in firstNumber) )
        secondNumberCombined = int( ''.join(str(e) for e in secondNumber) )
        
        combinedNumber = firstNumberCombined + secondNumberCombined
        combinedNumberList = [int(x) for x in str(combinedNumber)]
        combinedNumberList.reverse()
        
        finalAnswer = ListNode(combinedNumberList[0])
        tail = finalAnswer
        
        e = 1
        while e < len(combinedNumberList):
            tail.next = ListNode(combinedNumberList[e])
            tail = tail.next
            e+=1
            
        return finalAnswer
