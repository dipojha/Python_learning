def temperature_converter():
    print("Temperature Converter")
    print("---------------------")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    try:
        choice = int(input("Choose a conversion option (1-6): "))
        
        if choice < 1 or choice > 6:
            print("Invalid choice! Please select a valid option (1-6).")
            return

        temperature = float(input("Enter the temperature to convert: "))

        if choice == 1:
            # Celsius to Fahrenheit
            result = (temperature * 9/5) + 32
            print(f"{temperature}°C is equal to {result:.2f}°F")
        
        elif choice == 2:
            # Fahrenheit to Celsius
            result = (temperature - 32) * 5/9
            print(f"{temperature}°F is equal to {result:.2f}°C")
        
        elif choice == 3:
            # Celsius to Kelvin
            result = temperature + 273.15
            print(f"{temperature}°C is equal to {result:.2f}K")
        
        elif choice == 4:
            # Kelvin to Celsius
            result = temperature - 273.15
            print(f"{temperature}K is equal to {result:.2f}°C")
        
        elif choice == 5:
            # Fahrenheit to Kelvin
            result = (temperature - 32) * 5/9 + 273.15
            print(f"{temperature}°F is equal to {result:.2f}K")
        
        elif choice == 6:
            # Kelvin to Fahrenheit
            result = (temperature - 273.15) * 9/5 + 32
            print(f"{temperature}K is equal to {result:.2f}°F")
        
    except ValueError:
        print("Invalid input! Please enter numeric values only.")

# Run the temperature converter
temperature_converter()
