n = int(input("입력"))
end_num = n * n
cnt = 1
R_row, row = n - 1, 0
R_col, col= 0, n - 1
start_num_col, start_num_R_col = 1, 1
start_num_row, start_num_R_row = 0, 0
arr = [[0] * n for y in range(n)]
check = True
revers_check1, revers_check2 = False, False
while(cnt <= end_num) :
    if(check is True):
        if(revers_check1 is False):
            for i in range(1):
                for j in range(start_num_row, n):
                    arr[row][j] = cnt
                    cnt += 1
            revers_check1 = True
            start_num_row += 1
            row += 1
        else:
            for i in range(1):
                for j in reversed(range(start_num_R_row, n)):
                    arr[R_row][j] = cnt
                    cnt += 1
            revers_check1 = False
            start_num_R_row += 1
            R_row -= 1

        check = False
    else:
        if (revers_check2 is False):
            for i in range(1):
                for j in range(start_num_col, n):
                    arr[j][col] = cnt
                    cnt += 1
            revers_check2 = True
            col -= 1
            start_num_col += 1
            n -= 1
        else:
            for i in range(1):
                for j in reversed(range(start_num_R_col, n)):
                    arr[j][R_col] = cnt
                    cnt += 1
                revers_check2 = False
            R_col += 1
            start_num_R_col += 1

        check = True



for i in arr:
    for j in i:
        print(" ",j, end='')
    print()

