
memo = {
    0 : 0,
    1 : 1,
    2 : 2
}
def triple_step(n):
    if n not in memo:
        memo[n] = triple_step(n-1) + triple_step(n-2) + triple_step(n-3)
    return memo[n]

def test1():
    return triple_step(5)

def main():
    print test1()

if __name__ == "__main__":
    main()
