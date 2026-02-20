def main():
    while True:
        try:
            line = input("\nВведіть рік (або exit для виходу): ").strip().lower()
            if line == 'exit':
                break
            
            year = int(line)
            if year <= 0:
                print("Будь ласка, введіть рік нашої ери (більше 0).")
                continue
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

            if is_leap:
                status = "Високосний"
            else:
                status = "Не високосний"

            print(f"Результат: Рік {year} — {status}.")

            if not is_leap:
                next_year = year + 1
                while not ((next_year % 4 == 0 and next_year % 100 != 0) or (next_year % 400 == 0)):
                    next_year += 1
                print(f"Наступним високосним роком буде {next_year} (через {next_year - year} р)")
            else:
                print("Це і є високосний рік")

        except ValueError:
            print("Помилка: Введіть коректне ціле число.")

if __name__ == "__main__":
    main()