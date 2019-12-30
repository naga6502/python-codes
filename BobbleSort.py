def buble_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            # print(f'J: {j}')
            if nums[j] >= nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    return nums;


numbers = [5, 2, 9, 3, 6, 4]
print(buble_sort(numbers))
