def max_sub_array_of_size_k(nums, k):
    windowsum = sum(nums[:k])
    maxsum = windowsum
    for i in range(len(nums)-k):
        windowsum = windowsum-nums[i]+nums[i+k]
        maxsum = max(maxsum,windowsum)
    return maxsum