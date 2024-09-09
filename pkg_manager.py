import requests
import zipfile
import os
import shutil

def pkg_files():
    repo_name = "T-90val/file_pynext_update"
    file_name = input("Enter the file name (with extension): ")

    file_url = f'https://raw.githubusercontent.com/{repo_name}/main/{file_name}'

    response = requests.get(file_url)

    if response.status_code == 200:
        try:
            # Открываем файл для записи
            with open(file_name, 'wb') as f:
                f.write(response.content)
            print("File downloaded successfully.")
        except Exception as e:
            print("Error while saving the file:", e)
    else:
        print("Failed to download the file:", response.status_code)

if __name__ == '__main__':
    pkg_files()