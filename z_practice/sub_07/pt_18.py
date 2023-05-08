class City:
    a = ['Seoul', 'Incheon', 'Daejeon', 'Jeju']

str = ''
for i in City.a:
    if i == City.a[-1]:
        print(f'{i}\n=======')
    else:
        print(i)
    str += i[0]

print(str)