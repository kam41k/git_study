cnt = 0
for i in range(32, 128):
    cnt += 1
    if cnt % 10 != 0:
        print(f'{i}|{chr(i)}'.zfill(5), end='  ||  ')
    elif cnt % 10 == 0:
        print(f'{i}|{chr(i)}'.zfill(5))
