input_month = input()
input_day = int(input())

#season number ranges
winter = list(range(1221, 1232)) + list(range(101, 319))
spring = range(320,621)
summer = range(621,922)
autumn = range(922,1221)

#31 day months
month_day_31 = [100, 300, 500, 700, 800, 1000, 1200]
#30 day months
month_day_30 = [400, 600, 900, 1100]

#declare months = int
months = {
        'January': 100, 'February':200, 'March':300,
        'April':400, 'May':500, 'June':600, 
        'July':700, 'August':800, 'September':900, 
        'October':1000, 'November':1100, 'December':1200
        }

#search for input_month value in months dic
key_val = [val for key, val in months.items() if input_month in key]

#error check
if not key_val:
    print("Invalid")
    exit()

num = 0

for month in key_val:
    num = num*10 + month

date = int(month + input_day)

if input_day <= 0:
    print("Invalid")

elif month in month_day_31 and input_day > 31:
    print("Invalid")

elif month in month_day_30 and input_day > 30:
    print("Invalid")

elif month == 200 and input_day > 28:
    print("Invalid")
   
elif date in winter:
    print("Winter")

elif date in spring:
    print("Spring")

elif date in summer:
    print("Summer")

elif date in autumn:
    print("Autumn")
    
else:
    print("Invalid")
