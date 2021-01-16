def fsort(a, max):
    f = [0] * (max + 1)  # 0점도 포함을 위해 +1
    n = len(a)
    b = [0] * n
    for i in range(n):  # 도수 분포표
        f[a[i]] += 1
    for i in range(1, max + 1):  # 누적 분포표
        f[i] += f[i - 1]
    for i in range(n - 1, 0 - 1, -1):
        f[a[i]] -= 1    #(인덱스0부터 시작이므로 -1해야 자신위치를 찾을 뿐만 아니라 중복처리)
        b[f[a[i]]] = a[i]
    for i in range(n):
        a[i] = b[i]


def counting_sort(a):
    fsort(a, max(a))


a = [22, 5, 11, 32, 99, 68, 70]
counting_sort(a)
print(a)