def calculate_temperature(a, b, c, day):
    return a * (day ** 2) + b * day + c

a_coefficient = 2
b_coefficient = 5
c_coefficient = 3
input_day = 10

result = calculate_temperature(a_coefficient, b_coefficient, c_coefficient, input_day)
print(f"Temperature on day {input_day} is {result} degrees.")
