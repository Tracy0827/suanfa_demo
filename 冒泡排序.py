def bubbleSort(nums):
    for i in range(len(nums) - 1): # 遍历 len(nums)-1 次
        for j in range(len(nums) - i - 1): # 已排好序的部分不用再次遍历
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j] # Python 交换两个数不用中间变量
    return nums

nums = [10,2,4,7,1,6,3,5,9,8]
res = bubbleSort(nums)
print(res)