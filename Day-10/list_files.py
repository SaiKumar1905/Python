import os

def list_files_in_folder(folder):
    try:
        files=os.listdir(folder)
        return files,None
    
    except FileNotFoundError:
        return None,"file not found"
    
    except PermissionError:
        return None,"permission denied"


def main():
    folder_list=input("please provide the list of folder with space").split()
    
    for folder in folder_list:
        files,error_message= list_files_in_folder(folder)

        if files:
            print(f"files in {folder}:")

            for file in files:
                print(file)
        else :
            print(f"error in {folder}:{error_message}")

    
    
if __name__ == "__main__":
    main()
