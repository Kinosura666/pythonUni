import re

def get_ip_info(ip):
    octets = ip.split('.')
    first = int(octets[0])
    second = int(octets[1])
    
    if 1 <= first <= 126: ip_class = "Class A"
    elif 128 <= first <= 191: ip_class = "Class B"
    elif 192 <= first <= 223: ip_class = "Class C"
    elif 224 <= first <= 239: ip_class = "Class D"
    elif 240 <= first <= 255: ip_class = "Class E"
    else: ip_class = "Reserved"

    is_private = (
        (first == 10) or
        (first == 172 and 16 <= second <= 31) or
        (first == 192 and second == 168)
    )
    ip_type = "Private" if is_private else "Public"
    
    return f"{ip_class}, {ip_type}"

def main():
    print("Enter IP address (or press Enter to read from 'ip_input.txt'):")
    user_input = input("> ").strip()

    ip_list = []
    if user_input:
        ip_list.append(user_input)
    else:
        try:
            with open("ip_input.txt", "r") as f:
                ip_list = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print("File 'ip_input.txt' not found")
            return

    ip_pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    results = []
    print("\nProcessing results:")
    print("-" * 50)

    for ip in ip_list:
        if re.match(ip_pattern, ip):
            info = get_ip_info(ip)
            res_text = f"IP '{ip}' is valid. | {info}"
        else:
            res_text = f"IP '{ip}' is invalind. | Wrong format"
        
        print(res_text)
        results.append(res_text)

    with open("ip_result.txt", "w", encoding="utf-8") as f_out:
        f_out.write("\n".join(results))
    
    print("-" * 50)
    print(f"Total processed: {len(results)}. Results saved in 'ip_result.txt'")

if __name__ == "__main__":
    main()