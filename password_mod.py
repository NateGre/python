word = input()
password = ''


#could use the function .replace() as another option
#ex. word = word.replace('i','1').replace('a','@') etc.
for i in word:
    if i == 'i':
        password += '1'
    elif i == 'a':
        password += '@'
    elif i == 'm':
        password += 'M'
    elif i == 'B':
        password += '8'
    elif i == 's':
        password += '$'
    else:
        password += i

password += '!'

print(password)