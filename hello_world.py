def greet_user():
    name = input("Введите ваше имя: ").strip()  # Удаляение пробелов
    if name:  # Проверка, что имя не пустое
        print(f"Hello world from {name}")  # Используем f-строки для форматирования
    else:
        print("Имя не может быть пустым. Пожалуйста, введите ваше имя.")

if __name__ == "__main__":
    greet_user()
