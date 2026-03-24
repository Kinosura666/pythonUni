import os

def create_sample_file(filename: str) -> None:
    content = ["FIRST LINE", 
               "\n",
               "   \n",
               "Second\t LINE\n\n",
               "\t\n",
               "THIRD line"
               ]
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(content)
    print(f"Test file {filename} created")
    
def process_text_File(input_path: str, output_path: str) -> None:
    try:
        with open(input_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        if not lines:
            print("Input file is empty")
            return None
        
        processed_lines = [line.lower() for line in lines if line.strip()]
        
        with open(output_path,"w", encoding="utf-8") as file:
            file.writelines(processed_lines)
            
        print(f"Lines processed: {len(processed_lines)}")
        print(f"Result saved in {output_path}")
    except FileNotFoundError:
        print(f"File was not found at {input_path}")
        
def main():
    input_file = "input.txt"
    output_file = "output.txt"
    
    create_sample_file(input_file)
    process_text_File(input_file, output_file)
    
    if os.path.exists(output_file):
        print("Data inside:")
        with open(output_file, "r",encoding="utf-8") as file:
            print(file.read(),end="")
            
if __name__=="__main__":
    main()
    