import random


def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = int((low + high)/2)
        midVal = nums[mid]

        if midVal < target:
            low = mid + 1
        elif midVal > target:
            high = mid - 1
        else:
            return mid

    return ~low


maxLen = 10000
for i in range(1000):
    length = random.randint(0, maxLen)
    nums = random.sample(range(0, 10000), length)
    nums.sort()
    target = random.sample(nums, 1)[0]
    print(str(nums) + "," + str(target))
    ind = binarySearch(nums, target)
    print(str(ind))
    if target != nums[ind]:
        print("ERROR")
