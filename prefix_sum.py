nums = [2, 1, 3, 4, 5, 8, 1]

# calculate the prefix or running sum

prefix = [nums[0]]

for i in range(1, len(nums)):
    prefix.append(prefix[-1] + nums[i])

print(prefix)


prefix_sum = [0] * (len(nums) + 1)

print(prefix_sum)
print(nums)
for i in range(1, len(prefix_sum)):
    prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

print(prefix_sum)
