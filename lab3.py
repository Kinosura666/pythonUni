import random

def main():
    list_ints = [random.randint(1,100) for _ in range (5)]
    list_floats = [round(random.uniform(1.0, 50.0),2) for _ in range (5)]

    print(f"Generated list of Integers: {list_ints}")
    print(f"Generated list of Floats: {list_floats}")
    
    list_combined = list_ints + list_floats
    
    if list_combined:
        average_value = sum(list_combined) / len(list_combined)
    else:
        average_value = 0
        
    print(f"Combined list: {list_combined}")
    print(f"Total list length: {len(list_combined)}")
    print(f"Average value of all elements: {average_value}")
    
    print(f"Sorted data: {sorted(list_combined)}")


if __name__=="__main__":
    main()