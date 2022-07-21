def nats(n):
    yield n
    yield from nats(n+1)

def sieve(s):
    n = next(s)
    yield n
    yield from sieve(i for i in s if i % n != 0)

if __name__ == "__main__":
    p = sieve(nats(2))
    user_in = input(">")
    while user_in != "q":
        print(next(p))
        user_in = input(">")