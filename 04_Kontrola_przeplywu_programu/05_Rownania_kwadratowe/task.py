text = "Equation a*x**2 + b*x + c == 0"
print(text)
a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")
a = float(a)
b = float(b)
c = float(c)
result = b**2 - 4*a*c
if result > 0:
    x_1 = (-b - result**0.5) / (2 * a)
    x_2 = (-b + result**0.5) / (2 * a)
    print(f"Pierwiastki równania kwadratowego:\n"
    f"x_1 = {x_1}\n"
    f"x_2 = {x_2}")
elif result == 0:
    x_1 = (-b - result ** 0.5) / (2 * a)
    x_2 = (-b + result ** 0.5) / (2 * a)
    print(f"Pierwiastki równania kwadratowego:\n"
    f"x_1 = x_2 = {result}")
else:
    print("no solution")
