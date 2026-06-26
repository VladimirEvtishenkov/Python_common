import os

# Получаем текущую директорию
current_dir = os.getcwd()

# Проходим по всем файлам в текущей папке
for filename in os.listdir(current_dir):
    # Полный путь к файлу
    file_path = os.path.join(current_dir, filename)
    # Проверяем, что это файл
    if os.path.isfile(file_path):
        # Разделяем имя и расширение
        base_name, ext = os.path.splitext(filename)
        # Если расширение соответствует
        if ext.lower() in ['.log', '.data']:
            new_name = f"{base_name}_2{ext}"
            new_path = os.path.join(current_dir, new_name)
            # Переименовываем файл
            os.rename(file_path, new_path)
            print(f"Переименовали: {filename} -> {new_name}")