def binarysearch(nums, searhingnum):
    nums.sort()
    l = 0
    u = len(nums) - 1
    while l <= u:
        mid = (u + l) // 2
        if nums[mid] == searhingnum:
            return True
        else:
            if nums[mid] < searhingnum:
                l = mid + 1
            elif nums[mid] > searhingnum:
                u = mid - 1
    return False


numarr = [2, 5, 8, 1, 6]
result = binarysearch(numarr, 6)
if result:
    print("Given number is found in the list")
else:
    print("Given number is not found in the list")
