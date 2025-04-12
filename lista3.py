a=[2*x for x in range(1,10+1)]    ## numeros 1-20
print(a)
b=[(2*x)+1 for x in range(0,5)]    ## impares 1-10
print(b)
print([n for n in range(1,10,2)])  ## impares 1-10
d=(n for n in range (1,10,2))
mult3=[0 if num% 3== 0 else num for num in d]
print(mult3)
print([0 if num%3==0 else num for num in range(1,10,2)])