def selectionsort(nums):
    for i in range(len(nums)-1):
        minpos = i
        for j in range(i,len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

    return nums


numbers = [5, 2, 9, 3, 6, 4]
print(selectionsort(numbers))