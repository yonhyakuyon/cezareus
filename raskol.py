import openpyxl
from collections import Counter


def calculate_frequencies(text):
    """
    Подсчитывает частоту символов в тексте.
    """
    # Оставляем только буквы русского алфавита
    filtered_text = [char for char in text.lower() if "а" <= char <= "я" or char == "ё"]

    # Считаем частоты
    total_chars = len(filtered_text)
    frequencies = Counter(filtered_text)

    # Преобразуем частоты в доли
    return {char: count / total_chars for char, count in frequencies.items()}


def write_frequencies_to_excel(frequencies, output_file):
    """
    Записывает частоты символов в Excel-файл.
    """
    # Создаём новую рабочую книгу
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "freq"

    # Записываем заголовки
    sheet.append(["Symbol", "Freq"])

    # Записываем данные
    for char, freq in sorted(frequencies.items()):
        sheet.append([char, freq])

    # Сохраняем файл
    workbook.save(output_file)
    print(f"freq saved '{output_file}'.")


def analyze_text_and_save_to_excel(input_file, output_file):
    """
    Анализирует текст из файла и сохраняет частоты символов в Excel.
    """
    try:
        # Читаем текст из входного файла
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print("No input file")
        return

    # Подсчитываем частоты символов
    frequencies = calculate_frequencies(text)

    # Записываем частоты в Excel
    write_frequencies_to_excel(frequencies, output_file)


# Пример использования
input_path = "input.txt"  # Файл с текстом
output_path = "frequencies.xlsx"  # Excel-файл для записи частот

analyze_text_and_save_to_excel(input_path, output_path)
