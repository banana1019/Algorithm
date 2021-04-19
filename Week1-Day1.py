def two_sum(nums, target):
    for i in nums:
        for j in nums:
            if i + j == target:
                return [nums.index(i), nums.index(j)]
