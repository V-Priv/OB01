# Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач
# и вывода списка текущих (не выполненных) задач.

class Task: # класс задачи(описание задачи, срок выполнения и статус
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False # статус выполнения

    def mark_as_completed(self): # функция определения статуса задачи
        self.completed = True

    def __str__(self): # функция предоставления информации о стстусе задачи в виде строки
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description} - до {self.deadline}"


class TaskManager: # класс управления списком задач
    def __init__(self):
        self.tasks = [] # функция управления списком задач

    def add_task(self, description, deadline): # метод добавления задачи и её срока выполнения в список
        task = Task(description, deadline)
        self.tasks.append(task)

    def complete_task(self, task_number): # метод определения номера задачи из списка
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number].mark_as_completed()
        else:
            print("Неверный номер задачи.")

    def show_tasks(self, show_all=True): # метод показа всех задач из списка
        if not self.tasks:
            print("Список задач пуст.")
            return
        for i, task in enumerate(self.tasks):
            if show_all or not task.completed:
                print(f"{i}. {task}")

    def show_incomplete_tasks(self): # метод показа неисполненных задач
        self.show_tasks(show_all=False)


def main(): # функция для удобного проедоставления пользователю информации о всех задачах и их статусах
    task_manager = TaskManager()

    while True:
        print("\n1. Добавить задачу")
        print("2. Отметить задачу как выполненную")
        print("3. Показать все задачи")
        print("4. Показать невыполненные задачи")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            description = input("Введите описание задачи: ")
            deadline = input("Введите срок выполнения задачи: ")
            task_manager.add_task(description, deadline)
        elif choice == '2':
            task_manager.show_tasks()
            try:
                task_number = int(input("Введите номер задачи для отметки как выполненной: "))
                task_manager.complete_task(task_number)
            except ValueError:
                print("Пожалуйста, введите правильный номер задачи.")
        elif choice == '3':
            task_manager.show_tasks()
        elif choice == '4':
            task_manager.show_incomplete_tasks()
        elif choice == '5':
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__": # функция взаимодействия с пользователем
    main()