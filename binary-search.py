def binarySearch(arr, left, right, target):
    if left > right:
        return False
    mid = (left + right) // 2
    if arr[mid] == target:
        return True
    if target < arr[mid]:
        return binarySearch(arr, left, mid - 1, target)
    return binarySearch(arr, mid + 1, right, target)


def binarySearch(nums, left, right, target, side):
    if left > right:
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        if nums[mid + side] != target:
            return mid
        if side < 0:
            right = mid - 1
            return binarySearch(nums, left, mid - 1, target, side)
        else:
            left = mid + 1
            return binarySearch(nums, mid + 1, right, target, side)
    if nums[mid] > target:
        return binarySearch(nums, left, mid - 1, target, side)
    if nums[mid] < target:
        return binarySearch(nums, mid + 1, right, target, side)

if __name__ == "__main__":
    arr = [1,2,2,2,3]
    print(binarySearch(arr, 0, len(arr) - 1, 5, 1))