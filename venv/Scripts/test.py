from typing import Any, Sequence


def seq_search(seq: Sequence, Key: Any) -> int:

    for i in range(len(a)):
        if a[i] == Key:
            return i
        return -1

if __name__ == '__main__':
    num = int(input('원소 수 입력 :'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[i]: '))

    ky = int(input('검색값 입력'))

    idx = seq_search(x, ky)

    if idx == -1:
        print('no')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')