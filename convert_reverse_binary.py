usr_input = int(input())

while usr_input > 0:
    bin = int(usr_input % 2)
    print(bin, end=' ')
    usr_input = usr_input // 2

else:
    exit()