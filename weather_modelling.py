def calculate_temperature(a, b, c, day):
    return a * (day ** 2) + b * day + c

a_coefficient = float(input("Enter coefficient 'a': "))
b_coefficient = float(input("Enter coefficient 'b': "))
c_coefficient = float(input("Enter coefficient 'c': "))
input_day = int(input("Enter the day: "))

result = calculate_temperature(a_coefficient, b_coefficient, c_coefficient, input_day)
print(f"Temperature on day {input_day} is {result} degrees.")
