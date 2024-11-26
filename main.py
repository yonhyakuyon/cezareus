def caesar_cipher_with_custom_alphabet(input_file, output_file, custom_alphabet):
    # Оригинальный алфавит
    original_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    if len(custom_alphabet) != len(original_alphabet) or sorted(
        custom_alphabet
    ) != sorted(original_alphabet):
        print(
            "Ошибка: введённый алфавит некорректен. Проверьте, что он содержит все буквы русского алфавита в уникальном порядке."
        )
        return

    # Создаём таблицу замены для строчных и заглавных букв
    original_upper = original_alphabet.upper()
    custom_upper = custom_alphabet.upper()

    # Открываем входной файл
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print("Файл не найден. Проверьте путь к файлу.")
        return

    # Шифруем текст
    encrypted_text = []
    for char in text:
        if char in original_alphabet:
            encrypted_text.append(custom_alphabet[original_alphabet.index(char)])
        elif char in original_upper:
            encrypted_text.append(custom_upper[original_upper.index(char)])
        else:
            encrypted_text.append(char)

    # Записываем зашифрованный текст в выходной файл
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("".join(encrypted_text))

    print(f"Текст успешно зашифрован и сохранён в файл '{output_file}'.")


# Пример использования
input_path = "input.txt"  # Файл с исходным текстом
output_path = "output.txt"  # Файл для зашифрованного текста

# Введите пользовательский алфавит
print(
    "Введите новый алфавит для замены (например, 'гдеёжзийклмнопрстуфхцчшщъыьэюяабв'): "
)
custom_alphabet = input().strip()

caesar_cipher_with_custom_alphabet(input_path, output_path, custom_alphabet)
