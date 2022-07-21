from functools import cache


def palindromic_sequence():
    pass
"""
Strategy: L(i,j) is length of longest palindromic sequence x[i,...,j] i leq j

"""
def L(x,i,j):
    if i == j:
        return 1
    if i > j:
        return 0
    if x[i] == x[j]:
        if i + 1 == j:
            return 2
        else:
            return 2 + L(x, i + 1, j - 1)
    else:
        return max( L(x, i + 1, j),
                    L(x, i, j - 1))

def L_dp(x, i, j, dp):
    if f"{i}-{j}" in dp:
        return dp[f"{i}-{j}"]
    if i == j:
            return 1
    if i > j:
        return 0
    if x[i] == x[j]:
        if i + 1 == j:
            return 2
        else:
            return 2 + L_dp(x, i + 1, j - 1, dp)
    else:
        dp[f"{i}-{j}"] = max(L_dp(x, i + 1, j, dp),
                            L_dp(x, i, j - 1, dp))
        return dp[f"{i}-{j}"]


if __name__ == "__main__":
    words = ["underqualified", "turboventilator"]
    answers = ["deified", "rotator"]
    for i,v in enumerate(words):
        print(f"Checking {v}")
        assert len(answers[i]) == L_dp(v,0,len(v) - 1, dp = {})