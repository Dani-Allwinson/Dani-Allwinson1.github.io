# x=-b+-sqrt(b**2-4ac)/2a
# Equation will be ax**2+bx+c=0

a=int(input("Enter a :"))
b=int(input("Enter b :"))
c=int(input("Enter c :"))

sqrt=(((b**2)-(4*a*c))**0.5)
result1=(-b+sqrt)/2*a
print(complex(result1))
result2=(-b-sqrt)/2*a
print(complex(result2))