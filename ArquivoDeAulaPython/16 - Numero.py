# Tipos Numericos  chamar as funções interna do builtins



#print(dir(int))

#print(dir(float))

a = 5

b = 2.5

# imprimindo resultado float
print(a / b)

print(a + b)

print(a * b)

print(b.is_integer())

print(5.0.is_integer())


print(int.__add__(2,3))


# convert numero absoluto

print(abs(-2))