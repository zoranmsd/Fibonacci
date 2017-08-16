
number = int(input("How many Fibonacci numbers do you want to generate? "))
print("""You wanted""",number,"""Fibonacci numbers: """)
i = 1
if number == 0:
    fibonacci = []
elif number == 1:
    fibonacci = [1]
elif number == 2:
    fibonacci = [1,1]
elif number > 2:
    fibonacci = [1,1]
while i < (number - 1):
    fibonacci.append(fibonacci[i] + fibonacci[i-1])
    i += 1
print(fibonacci)