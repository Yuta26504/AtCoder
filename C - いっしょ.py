from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
N = int(input())
a = list(map(int, input().split()))

avg = int(Decimal(str(sum(a) / N)).quantize(Decimal("0"), rounding=ROUND_HALF_UP))

ans = 0
for i in a:
    ans += pow(i-avg, 2)

print(ans)