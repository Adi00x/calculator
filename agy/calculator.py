"""Interactive Calculator & Unit Converter

A menu-driven CLI program that handles:
- Basic arithmetic (+, -, *, /)
- Unit conversions (km to miles, Celsius to Fahrenheit)
"""

def show_menu():
    """Display the main menu options."""
    print("\n" + "=" * 40)
    print("   CALCULATOR & UNIT CONVERTER")
    print("=" * 40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Kilometers to Miles")
    print("6. Celsius to Fahrenheit")
    print("7. Quit")
    print("-" * 40)


def get_number(prompt: str) -> float:
    """Get a valid number from the user."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_menu_choice() -> int:
    """Get a valid menu choice from the user."""
    while True:
        try:
            choice = int(input("Enter your choice (1-7): "))
            if 1 <= choice <= 7:
                return choice
            print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b. Raises ValueError if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def km_to_miles(km: float) -> float:
    """Convert kilometers to miles."""
    return km * 0.621371


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def handle_arithmetic(choice: int):
    """Handle arithmetic operations based on user's choice."""
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")

    try:
        if choice == 1:
            result = add(a, b)
            operation = "+"
        elif choice == 2:
            result = subtract(a, b)
            operation = "-"
        elif choice == 3:
            result = multiply(a, b)
            operation = "*"
        elif choice == 4:
            result = divide(a, b)
            operation = "/"

        print(f"Result: {a} {operation} {b} = {result}")

    except ValueError as e:
        print(f"Error: {e}")


def handle_conversion(choice: int):
    """Handle unit conversions based on user's choice."""
    if choice == 5:
        km = get_number("Enter distance in kilometers: ")
        miles = km_to_miles(km)
        print(f"{km} km = {miles:.4f} miles")
    elif choice == 6:
        celsius = get_number("Enter temperature in Celsius: ")
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C = {fahrenheit:.2f}°F")


def main():
    """Main program loop."""
    print("Welcome to the Calculator & Unit Converter!")

    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == 7:
            print("Thank you for using the calculator. Goodbye!")
            break
        elif 1 <= choice <= 4:
            handle_arithmetic(choice)
        elif 5 <= choice <= 6:
            handle_conversion(choice)


if __name__ == "__main__":
    main()