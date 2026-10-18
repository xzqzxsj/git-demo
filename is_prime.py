import math
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:      # 排除偶数
        return False

    limit = int(math.sqrt(n))
    for i in range(3, limit + 1, 2):  # 只检查奇数
        if n % i == 0:
            return False
    return True
