def _get_change_making_matrix(set_of_coins, r):
    m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]
    for i in range(1, r+1):
        m[0][i] = float('inf')
    return m

def make_change(coins, n):
    m = _get_change_making_matrix(coins,n)
    for x in m:
        print(x)
    for c, coin in enumerate(coins, 1):
        for r in range(1, n+1):
            if coin == r:
                m[c][r] = 1
            elif coin > r:
                m[c][r] = m[c-1][r]
            else:
                m[c][r] = min(m[c-1][r], 1 + m[c][r-coin])
    return m[-1][-1]

if __name__ == "__main__":
    coins = [1,5,10, 25, 50]
    total = 5
    print(make_change(coins, total))