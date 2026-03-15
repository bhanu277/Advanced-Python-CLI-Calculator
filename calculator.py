import math

history = []

def save_history(entry):
    history.append(entry)
    with open("history.txt", "a") as file:
        file.write(entry + "\n")

while True:

    print("\n===== Advanced Python Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. sin(x)")
    print("8. cos(x)")
    print("9. log(x)")
    print("10. factorial")
    print("11. Exit")

    choice = input("Choose option: ")

    if choice == "11":
        print("Goodbye!")
        break