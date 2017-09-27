a=23
print(type(a))
print(isinstance(a,int))

b=False
print(type(b))

b=0b1101
c=0o23
d=0x23

print(a,b,c,d)

# 3.x 이상에서는 int, long 합쳐짐
e=2**1024
print(type(e))
print(e)

#변홚함수
print(oct(38))
print(hex(38))
print(bin(38))