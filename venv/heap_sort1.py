def heap_sort(a):

    def down_heap(a, left, right):
        temp = a[left]  #부모값

        parent = left
        while parent < (right + 1) // 2:    #제일 아래 단계인지 확인
            cl = parent * 2 + 1             #왼쪽자리
            cr = cl +1                      #오른쪽자리
            child = cr if cr <= right and a[cr] > a[cl] else cl
            if temp >= a[child]:    #부모와 자식값비교
                break
            a[parent] = a[child]    #부모 자식 값 교환
            parent = child          #아래 자식이 더있나 확인하기위함
        a[parent] = temp

    n = len(a)


    for i in range((n - 1) // 2, -1, -1):
        down_heap(a, i, n - 1) #배열을 힙으로 바꾸는 과정


    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0] #루트값과 배열의 마지막 원소 값 교환
        down_heap(a, 0, i - 1)  #0부터 n - i까지 힙 정렬


a = [6, 4, 3, 7, 1, 9, 8]
heap_sort(a)
print(a)