#Merge Sort.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        def merged(nums1, nums2):
            sorted_array = []
            while len(nums1) > 0 and len(nums2) > 0:
                if nums1[0] < nums2[0]:
                    sorted_array.append(nums1.pop(0))
                else:
                    sorted_array.append(nums2.pop(0))
            sorted_array.extend(nums1)
            sorted_array.extend(nums2)
            return sorted_array
        
        if total %2 != 0:
            return merged(nums1, nums2)[total//2]
        else:
            return sum(merged(nums1, nums2)[total//2-1:total//2+1])/2


#Other Solution
class Solution_median_native:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return median(sorted(nums1 + nums2))
