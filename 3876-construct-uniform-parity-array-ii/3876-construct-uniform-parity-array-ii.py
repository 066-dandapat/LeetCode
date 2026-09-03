class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        # Step 1: Find the smallest odd number in the array
        min_odd = float('inf')
        for num in nums1:
            if num % 2 == 1:
                min_odd = min(min_odd, num)
        
        # Step 2: If there are no odd numbers, all are even (already uniform parity)
        if min_odd == float('inf'):
            return True
            
        # Step 3: Check if any even number is smaller than the minimum odd number
        for num in nums1:
            if num % 2 == 0 and num < min_odd:
                return False
                
        return True
