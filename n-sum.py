def n_sum(nums,target):
    def findNSum(l, r, target, N, result, results):
        if r - l + 1 < N or N < 2 or target < nums[l] * N or target > nums[r] * N:
            return
        if N == 2:
            while l < r:
                sum = nums[l] + nums[r]
                if sum == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif sum < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(l, r + 1):
                if i == l or (i > l and nums[i - 1] != nums[i]):
                    findNSum(i + 1, r, target - nums[i], N - 1, result+[nums[i]], results)
    nums.sort()
    results = []
    findNSum(0, len(nums) - 1, target, 4, [], results)
    return results

if __name__ == "__main__":
    print(n_sum([4,1,2,-1,1,-3],1))
    print(n_sum([2,0,-1,1,-2,2],2))
    print(n_sum([1,0,-1,0,-2,2],0))
    print(n_sum([0,0,0,0,0],0))