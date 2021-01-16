from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)#앞부분 정렬
            _merge_sort(a, center + 1, right)#뒷부분 정렬

            p = j = 0
            i = k = left

            while i <= center:         #배열 a의 앞부분을 버퍼에 넣어줌
                buff[p] = a[i]
                p += 1
                i += 1

            while i <= right and j < p:
                if buff[j] <= a[i]:     #앞부분이 뒷부분보다 작으면 다시 배열 a의 앞부분을 넣어줌
                    a[k] = buff[j]
                    j += 1
                else:                   #앞부분이 뒷부분보다 크면 뒷부분의 값을 앞부분에 넣어줌
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p:                # 앞부분이 뒷부분보다 컸으면 빈 뒷부분값에 버퍼에남은값을 배열 a의 넣어줌
                a[k] = buff[j]
                k += 1
                j += 1


    n = len(a)
    buff = [None] * n
    _merge_sort(a, 0 , n - 1)
    del buff

if __name__ == '__main__':
    print('병합 정렬')
    num = int(input('원소 수 입력 : '))
    x = [None] * num
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    merge_sort(x)

    for i in range(num):
        print(f'x[{i}] = {x[i]}')

