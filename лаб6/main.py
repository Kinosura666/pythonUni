import pandas as pd
import json

sample_list = ["Python", "Excel", "JSON", "CSV"]
sample_dict = {"course": "Python", "status": "In Progress"}

def work_with_json():
    data = {
        "students": [
            {"id": 1, "name": "Student1", "grade": 95},
            {"id": 2, "name": "Student2", "grade": 88}
        ]
    }
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    with open('data.json', 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
    
    loaded_data['students'].append({"id": 3, "name": "Student3", "grade": 92})
    loaded_data['students'][0]['grade'] = 100
    loaded_data['students'] = [s for s in loaded_data['students'] if s['name'] != "Student2"]

    with open('updated_data.json', 'w', encoding='utf-8') as f:
        json.dump(loaded_data, f, ensure_ascii=False, indent=4)
    print("JSON succeeded")

def work_with_csv():
    df = pd.DataFrame({
        'Name': ['Name1', 'Name2', 'Name3'],
        'Age': [25, 30, 35],
        'City': ['Kyiv', 'Poltava', 'Kharkiv']
    })
    df.to_csv('data.csv', index=False)

    df_csv = pd.read_csv('data.csv')
    
    new_row = pd.DataFrame([{'Name': 'Name4', 'Age': 28, 'City': 'Lviv'}])
    df_csv = pd.concat([df_csv, new_row], ignore_index=True)
    
    df_csv = df_csv[df_csv['Age'] <= 30]

    df_csv.to_csv('updated_data.csv', index=False)
    print("CSV succeeded")


def work_with_excel():
    df_test = pd.DataFrame({'Product': ['A', 'B', 'C'], 'Price': [100, 200, 300]})
    df_test.to_excel('data.xlsx', index=False)

    df_ex = pd.read_excel('data.xlsx')
    
    filtered_df = df_ex[df_ex['Price'] > 150].sort_values(by='Price', ascending=False)
    
    filtered_df.to_excel('processed_data.xlsx', index=False)
    print("Excel succeeded")

def csv_to_json(csv_file, json_file):
    df = pd.read_csv(csv_file)
    df.to_json(json_file, orient='records', force_ascii=False, indent=4)
    print(f"Convertation {csv_file} -> {json_file} succeeded.")

def sorting_csv():
    df = pd.read_csv('updated_data.csv')

    extra_data = pd.DataFrame([
        {'Name': 'Zahar', 'Age': 19, 'City': 'Kyiv'},
        {'Name': 'Anna', 'Age': 22, 'City': 'Kyiv'},
        {'Name': 'Borys', 'Age': 30, 'City': 'Lviv'}
    ])
    df = pd.concat([df, extra_data], ignore_index=True)

    df_sorted = df.sort_values(by=['City', 'Age'], ascending=[True, True])
    df_sorted['Category'] = df_sorted['Age'].apply(lambda x: 'Junior' if x < 25 else 'Senior')

    df_sorted.to_csv('sorted_data.csv', index=False)
    print("Sorting succeeded.")
    
def main():
    work_with_json()
    work_with_csv()
    work_with_excel()
    csv_to_json('updated_data.csv', 'converted_from_csv.json')
    sorting_csv()

if __name__ == "__main__":
    main()
    