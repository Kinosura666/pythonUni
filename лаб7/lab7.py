def main():
    input_file = "data.txt"
    log_file = "log.txt"
    valid_file = "valid_data.txt"

    with open(input_file, "w", encoding="utf-8") as f:
        f.write("100:Milk\n")
        f.write("200:Bread\n")
        f.write("100:Duplicate_ID\n")
        f.write("300:\n")
        f.write("Error:Id not number\n")
        f.write("50:Cheese\n")

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        valid_lines = []
        used_ids = [] 
        total_count = len(lines)

        for i, line in enumerate(lines, 1):
            line = line.strip()
            if not line: continue

            try: 
                if ":" not in line:
                    raise ValueError("Separator ':' not found")
                
                parts = line.split(":")
                
                if not parts[1].strip():
                    raise ValueError("Item name is empty")

                item_id = int(parts[0])

                if item_id in used_ids:
                    raise ValueError(f"Duplicate ID found: {item_id}")
                
                used_ids.append(item_id)
                valid_lines.append(line)

            except ValueError as e:
                error_msg = f"Line {i} ({line}): {e}"
                print(f" [LOGGED] {error_msg}")

                with open(log_file, "a", encoding="utf-8") as log:
                    log.write(error_msg + "\n")

        with open(valid_file, "w", encoding="utf-8") as f_valid:
            for item in valid_lines:
                f_valid.write(item + "\n")

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        success_percent = (len(valid_lines) / total_count) * 100 if total_count > 0 else 0
        print(f"\n--- Statistics ---")
        print(f"Processed: {total_count} lines")
        print(f"Valid: {len(valid_lines)} items")
        print(f"Accuracy: {success_percent:.1f}%")
    finally:
        print("Task finished")

if __name__ == "__main__":
    main()