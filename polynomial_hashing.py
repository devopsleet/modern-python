import math

P = 31
N = 10 ** 5
PP = [1] * (N+1)
MOD = 10 ** 9 + 7

def main():
    for i in range(1,N+1):
        PP[i] = (PP[i-1] * P) % MOD

def polynomial_hash(s: str)->int:
    ans = 0
    for i in range(len(s)):
        ans = (ans + (ord(s[i]) - ord('a') + 1)*PP[i])%MOD
    return ans


if __name__ == "__main__":
    main()
    s = input("Enter the string ")
    output = polynomial_hash(s)
    print(output)
