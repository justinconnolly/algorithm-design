def xsubset_total(A, sum):
    if sum == 0:
        return True
    if len(A) == 0:
        return False
    return any([subset_total(A[1:], sum), subset_total(A[1:], sum - A[0]) if sum >= A[0] else False])


def subset_total(A, sum, i, dp):
    if f"{sum}-{i}" in dp:
        return dp[f"{sum}-{i}"]
    if sum == 0:
        return 1
    if sum < 0:
        return 0
    if i < 0:
        return 0
    if sum < A[i]:
        ret_val =  subset_total(A, sum, i - 1, dp)
    else:
       ret_val = subset_total(A, sum - A[i], i - 1, dp) + subset_total(A, sum, i - 1, dp)
    dp[f"{sum}-{i}"] = ret_val   
    return ret_val
    

if __name__ == "__main__":
    numbers = [[2,5,7,8,9], [3,4,3,1], [2,3,3,6,10]]
    totals = [21,25, 16]
    answers = [1,0,2]
    dp = {}
    for i, v in enumerate(numbers):
        print(f"{v}: {subset_total(v, totals[i], len(v) - 1, dp)}")
        assert answers[i] == subset_total(v,totals[i], len(v) - 1, dp)