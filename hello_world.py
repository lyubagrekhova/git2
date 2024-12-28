def greet_user():
    name = input("Введите ваше имя: ").strip()
    if name: 
        print(f"Hello world from {name}")
    else:
        print("Имя не может быть пустым. Пожалуйста, введите ваше имя.")

if __name__ == "__main__":
    greet_user()