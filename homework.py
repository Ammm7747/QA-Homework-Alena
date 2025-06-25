
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Домашнее задание: Работа с Git, GitHub и локальным репозиторием

homework = {
    "author": "Alena Moriakova",
    "topic": "Загрузка локального проекта на GitHub и работа с git",
    "repository": {
        "name": "QA-Homework-Alena",
        "url": "https://github.com/Ammm7747/QA-Homework-Alena.git"
    },
    "status": "выполнено",
    "steps": [
        {
            "step": 1,
            "title": "Создание репозитория на GitHub",
            "description": "Создан репозиторий с именем 'QA-Homework-Alena' без добавления README.md"
        },
        {
            "step": 2,
            "title": "Инициализация локального проекта",
            "description": "Создана папка, инициализирован git, добавлен и закоммичен файл README.md",
            "commands": [
                "mkdir QA-Homework-Alena",
                "cd QA-Homework-Alena",
                "echo \"# QA Homework\" > README.md",
                "git init",
                "git add README.md",
                "git commit -m \"Initial commit\"",
                "git remote add origin https://github.com/Ammm7747/QA-Homework-Alena.git",
                "git push -u origin main"
            ]
        },
        {
            "step": 3,
            "title": "Изменения и пуш",
            "description": "Добавлен файл cat.py, закоммичен и отправлен в GitHub",
            "commands": [
                "echo \"print('Hello from Cat')\" > cat.py",
                "git add cat.py",
                "git commit -m \"Add cat.py\"",
                "git push"
            ]
        },
        {
            "step": 4,
            "title": "Проверка результата",
            "description": "Убедиться, что файл отображается на GitHub",
            "check_url": "https://github.com/Ammm7747/QA-Homework-Alena/blob/main/cat.py"
        }
    ]
}

# Вывод результата
print(f"\nДомашнее задание по теме: {homework['topic']}")
print(f"Автор: {homework['author']}")
print(f"Ссылка на репозиторий: {homework['repository']['url']}\n")

for step in homework["steps"]:
    print(f"Шаг {step['step']}: {step['title']}")
    print(f"Описание: {step['description']}")
    if "commands" in step:
        print("Выполненные команды:")
        for cmd in step["commands"]:
            print(f"  - {cmd}")
    if "check_url" in step:
        print(f"Проверить результат: {step['check_url']}")
    print()
