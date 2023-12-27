class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        arr = []

        left1 = left2 = 0

        while left1 < len(nums1) and left2 < len(nums2):
            if nums1[left1] == nums2[left2]:
                arr.append(nums1[left1])
                left1 += 1
                left2 += 1
            elif nums1[left1] > nums2[left2]:
                left2 += 1
            else:
                left1 += 1

        return arr

