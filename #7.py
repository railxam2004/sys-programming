import base64
import os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

# функция для кодирования одного файла в Base64
def encode_file(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data)
        # возвращаем строку Base64
        return file_path, encoded.decode("utf-8")
    except Exception as e:
        return file_path, f"Ошибка: {e}"
урурымвтототмвыом
# функция для параллельного кодирования
def encode_multiple_files(file_list):
    results = {}
    num_workers = os.cpu_count()  # количество ядер процессора
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        for file_path, encoded_data in executor.map(encode_file, file_list):
            results[file_path] = encoded_data
    return results

if __name__ == "__main__":
    # пользователь вводит пути к файлам через пробел
    files_input = input("Введите пути к файлам через пробел: ").split()
    files = [Path(f) for f in files_input if Path(f).exists()]

    if not files:
        print("Нет доступных файлов для кодирования.")
    else:
        encoded_files = encode_multiple_files(files)
        for name, data in encoded_files.items():
            print(f"\nФайл: {name}")
            if data.startswith("Ошибка"):
                print(data)
            else:
                print(f"Первые 60 символов Base64: {data[:60]}...")
