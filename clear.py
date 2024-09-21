import os
import shutil


def delete_files_in_folder(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if "gitkeep" in file_path:
                continue
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            else:
                shutil.rmtree(file_path)
                print(f"Deleted dir: {file_path}")
    except FileNotFoundError:
        print(f"Folder not found: {folder_path}")
    except PermissionError:
        print(f"Permission error while deleting files in: {folder_path}")


if __name__ == "__main__":
    for folder in os.listdir("output"):
        delete_files_in_folder("output/" + folder)
    try:
        os.remove("main.spec")
    except FileNotFoundError:
        pass
    print("Done!")
