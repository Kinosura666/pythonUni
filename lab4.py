import random
def main():
    test_values = [round(random.uniform(0.0,100.0),2) for _ in range (15)]
    for val in test_values:
        print(f"inches: {val} \t|\tcm: {inches_to_cm(val)}")
       
    results_cm = [] 
    
    for i, inch_val in enumerate(test_values, 1):
        cm_val = inches_to_cm(inch_val)
        results_cm.append(cm_val)
        print(f"{i:<3} | {inch_val:>6} inch | {cm_val:>6} cm")

    stats(results_cm)    
    
def inches_to_cm(inches: float) -> float:
    """
    cm = inches * 2.54
    """
    if inches < 0:
        return 0.0
    return round(inches*2.54,2)

def stats(data: list[float]) -> None:
    if not data:
        print("List is empty")
        return
    print(f"Max value: {max(data)} cm")
    print(f"Min value: {min(data)} cm")
    print(f"Average value: {sum(data)/len(data)} cm")
    

if __name__=="__main__":
    main()