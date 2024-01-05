# 　素数を見つける（エラトステネスのふるい）

n = 100
nums = [i for i in range(n + 1)]

root_n = int(n ** 0.5)
for i in range(2, root_n + 1):
    if nums[i] != 0:
        for j in range(i, n+1):
            if i*j >= n+1:
                break
            nums[i*j] = 0

primes = sorted(set(nums))[2:]

print(primes)
print(len(primes))