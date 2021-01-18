print("Перша константа", False)
print("Друга константа", None)
print("Третя константа", Ellipsis)

print(abs(-10.6), f" {abs(10.6)}")
print(bin(3254))
print(float('-1.15'))

A = False
print("А = True " if A else "A = False")
A = True
print("А = True " if A else "A = False")

B = 0
try:
    print("Що буде якщо", 5/B, "?")
except Exception as B:
    print(B)
finally:
    print ("А вот воно що!")

with open("text.txt", "r") as f:
    for line in f:
        print(line)

this_is_lambda = lambda first, last: f'Цей код написав: {first} {last}'
print("Це просто функція:", this_is_lambda)
print("Це її виклик:", this_is_lambda('Віктор', 'Сугерей'))
