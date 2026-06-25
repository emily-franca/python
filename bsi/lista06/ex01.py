def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    return celsius

temp_f = float(input("Enter temperature in Fahrenheit: "))
temp_c = convert_to_celsius(temp_f)
print(f"A temperatura em Celsius é: {temp_c:.2f}°C")