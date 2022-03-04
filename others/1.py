print('Hello world!')

a=10
print(type(a))
a+=2
print(type(a))
a+=2.5
print(type(a))
print(a)

a=10
print(type(a))
a=10.3
print(type(a))
a=True
print(type(a))

a=1
b=2
c=3
d=a+b+c
print(d)

a='abcd'
b='ooooo'
c=a+b
print(c)
c*=20
print(c)
print(b+str(30))

print('Your name is',input('Please input your name:'))

print(int(input())*int(input()))

a=10
if a>10:
    print('a')
else:
    print('b')

a=100
if a>90:
    print('A')
elif a>80:
    print('B')
elif a>60:
    print('C')
else:
    print('D')
