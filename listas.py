a=["juna",20,1.8,True]
print(a[len(a)-1])
print(a[-1])
print(a[-2])
print(a[-3])
b=[4,2,3,6]
print(len(b))
print(sum(b))
print(max(b))
print(min(b))
print(sum(b)/len(b))
c=a+b
print(c)
for x in b :
    print(x )
#### RESTRUCTURACION 
z="mesa"
x="cabeza"
print(z,x)
z,x=x,z
print(z,x)
def suma5(e,f):
    return e+5,f+5
print(suma5(2,5))

busca =6
if busca in b  :  #[4,2,3,6]
    print("encontrado")
    