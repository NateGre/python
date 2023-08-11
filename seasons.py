input_month = input()
input_day = int(input())

#season number ranges
winter = [(1221,1231), (101,131), (201,228), (301,319)]
spring = [(321,331), (401,430), (501,531), (601,620)]
summer = [(621,631), (701,731), (801,831), (901,921)]
autumn = [(922,930), (1001,1031), (1101,1130), (1201,1220)]

#declare months = int
months = {'January': 1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}

#search for input_month value in months dic
key_val = [val for key, val in months.items() if input_month in key]

#error check
if not key_val:
    print("Invalid")

if input_day > 31:
    print("Invalid")

num = 0
for month in key_val:
    num = num*10 + month
    month = month * 100
    date = int(month + input_day)

if date in winter:
    print(date,"Winter")

if date in spring:
    print("Spring")

if date in summer:
    print("Summer")

if date in autumn:
    print("Autumn")
    
else:
    print("Invalid")

