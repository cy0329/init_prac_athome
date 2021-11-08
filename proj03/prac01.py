"""
입력한 n에 대해 n의 약수들의 합 구하기
"""

for n in range(0, 3001):

    def sum_cal(n):
        x = 0
        for i in range(1, n + 1):
            if n % i == 0:
                x += i
        return x


n = int(input("약수의 합을 구할 수 : "))
print(sum_cal(n))
