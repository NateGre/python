listlength = int(input())

num_list = []

for i in range(0,listlength):
    num = float(input())
    num_list.append(num)

divide = max(num_list)

for num in num_list:
    newnum = num / divide
    print(f'{newnum:.2f}')