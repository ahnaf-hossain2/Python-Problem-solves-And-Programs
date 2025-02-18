def tempConvert_C_to_F(temp):
    return (9/5 * temp) + 32

temp = float(input("Enter the temperature in Celsius: "))
converted = tempConvert_C_to_F(temp)
print("Temperature in Fahrenheit is: ", round(converted, 2))
