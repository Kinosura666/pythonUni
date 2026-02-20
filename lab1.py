def main():
    try:
        a = float(input("Введіть перше число (a): "))
        b = float(input("Введіть друге число (b): "))

        print(f"Додавання: {a} + {b} = {a + b}")
        print(f"Віднімання: {a} - {b} = {a - b}")
        print(f"Множення: {a} * {b} = {a * b}")

        if b != 0:
            print(f"Ділення: {a} / {b} = {a / b}")
        else:
            print("Ділення: На 0 ділити не можна")

        print("\n--- Індивідуальне завдання ---")

        if b != 0 and a % b == 0:
            print(f"Число {b} є дільником числа {a}.")
        elif a != 0 and b % a == 0:
            print(f"Число {a} є дільником числа {b}.")
        else:
            print("Жодне з чисел не є дільником іншого")

    except ValueError:
        print("Помилка: Вводьте тільки цифри")

if __name__ == "__main__":
    main()