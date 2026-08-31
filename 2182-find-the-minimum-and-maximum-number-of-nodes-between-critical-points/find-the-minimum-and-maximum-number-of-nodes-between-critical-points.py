# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        first = -1
        prev_critical = -1
        min_dist = float('inf')

        prev = head
        curr = head.next
        pos = 1

        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):

                if first == -1:
                    first = pos
                else:
                    min_dist = min(min_dist, pos - prev_critical)

                prev_critical = pos

            prev = curr
            curr = curr.next
            pos += 1

        if first == -1 or prev_critical == first:
            return [-1, -1]

        return [min_dist, prev_critical - first]