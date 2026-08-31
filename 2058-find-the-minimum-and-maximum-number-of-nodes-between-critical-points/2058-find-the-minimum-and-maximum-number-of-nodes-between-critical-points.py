class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        prev = head
        curr = head.next
    
        index = 1
        first = -1
        last = -1
        min_dist = float('inf')
        
        while curr.next:
            next_node = curr.next
            
            # Check if curr is a local maximum or local minimum
            if ((curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)):
                
                if first == -1:
                    first = index
                else:
                    min_dist = min(min_dist, index - last)
                
                last = index
            
            prev = curr
            curr = next_node
            index += 1
        
        # Fewer than 2 critical points
        if first == -1 or first == last:
            return [-1, -1]
        
        max_dist = last - first
        
        return [min_dist, max_dist]