numbers = []
n = input("Enter n: ")
n = int(n)
result = 0
for i in range(n):
    number = input(f"Enter number: ")
    number = float(number)
    numbers.append(number)
result += number
mean = result / n
print("Entered numbers: ")
for number in numbers:
    print(number)
print(f"Sum numbers: {result}")
print(f" Mean numbers: {mean}")

