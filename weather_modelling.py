def calculate_temperature(a, b, c, day):
    return a * (day ** 2) + b * day + c

with open('coefficients_multiple.csv', 'r') as file:
    lines = file.readlines()
    for line in lines:
        a_coefficient, b_coefficient, c_coefficient = map(float, line.strip().split(','))
        input_day = int(input("Enter the day: "))
        result = calculate_temperature(a_coefficient, b_coefficient, c_coefficient, input_day)
        print(f"Temperature on day {input_day} is {result} degrees.")

result = calculate_temperature(a_coefficient, b_coefficient, c_coefficient, input_day)
print(f"Temperature on day {input_day} is {result} degrees.")
