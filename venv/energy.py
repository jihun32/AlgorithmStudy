
def energy_charge(a: list) -> int:
    n = len(a)
    j = 0
    max = 0
    if n == 2:
        return 0

    for i in range(n - 2):
        j = i + 2
        if a[i] * a[j] > max:
            max = a[i] * a[j]
            del_index = i + 1
    del a[del_index]
    return max + energy_charge(a)

num = int(input())
x = num * [None]
for i in range(num):
    x[i] = int(input())

print(energy_charge(x))