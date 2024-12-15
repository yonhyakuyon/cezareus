import openpyxl


def load_frequencies_from_excel(file_path):
    """
    Загружает частоты символов из Excel-файла.
    Предполагается, что файл содержит два столбца:
    1. Символ
    2. Частота
    """
    frequencies = {}
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        for row in sheet.iter_rows(min_row=2, max_col=2, values_only=True):
            char, freq = row
            if isinstance(char, str) and len(char) == 1:
                frequencies[char] = freq
    except FileNotFoundError:
        print("No file")
    except Exception as e:
        print(f"Excel reading error {e}")
    return frequencies


def decrypt_text_by_frequency(encrypted_text, symbol_frequencies):
    """
    Расшифровывает текст на основе частотного анализа.
    """
    # Сортируем символы по убыванию частоты в зашифрованном тексте
    encrypted_counts = {}
    for char in encrypted_text:
        if char.isalpha():  # Учитываем только буквы
            encrypted_counts[char] = encrypted_counts.get(char, 0) + 1

    # Сортируем символы в зашифрованном тексте по частоте
    sorted_encrypted_chars = sorted(
        encrypted_counts, key=encrypted_counts.get, reverse=True
    )

    # Сортируем символы русского алфавита по частоте из Excel
    sorted_real_chars = sorted(
        symbol_frequencies, key=symbol_frequencies.get, reverse=True
    )

    # Создаём таблицу замены
    decrypt_map = {}
    for enc_char, real_char in zip(sorted_encrypted_chars, sorted_real_chars):
        decrypt_map[enc_char] = real_char

    # Дешифруем текст
    decrypted_text = "".join(decrypt_map.get(char, char) for char in encrypted_text)

    return decrypted_text


def decrypt_text_from_file(input_file, output_file, excel_file):
    """
    Дешифрует текст из входного файла, используя частотный анализ, и сохраняет результат в выходной файл.
    """
    # Загружаем частоты символов из Excel
    symbol_frequencies = load_frequencies_from_excel(excel_file)
    if not symbol_frequencies:
        print("No freq")
        return

    # Читаем зашифрованный текст
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            encrypted_text = f.read()
    except FileNotFoundError:
        print("No input file")
        return

    # Дешифруем текст
    decrypted_text = decrypt_text_by_frequency(encrypted_text, symbol_frequencies)

    # Сохраняем результат
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(decrypted_text)

    print(f"Done '{output_file}'.")


# Пример использования
input_path = "output.txt"  # Файл с зашифрованным текстом
output_path = "decrypted.txt"  # Файл для расшифрованного текста
print("Выберете по какой статистике сделать криптоанализ")
print(
    'нажмите "1" если по общей статистике русского языка, нажмите "2" для криптоанализа по статистике исходного текста'
)
choise = int(input())
if choise == 1:
    excel_path = "freq.xlsx"  # Excel-файл с частотами символов
elif choise == 2:
    excel_path = "frequencies.xlsx"  # Excel-файл с частотами символов

decrypt_text_from_file(input_path, output_path, excel_path)
