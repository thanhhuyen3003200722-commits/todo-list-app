# todo-list-app
Một ứng dụng To-Do List đơn giản bằng Python.

tasks = []


def add_task(task_name):
    """Thêm công việc mới."""
    tasks.append({
        "name": task_name,
        "completed": False
    })
    print(f"Đã thêm công việc: {task_name}")


def list_tasks():
    """Hiển thị danh sách công việc."""
    if not tasks:
        print("Danh sách công việc đang trống.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{index}. {status} {task['name']}")


def complete_task(task_index):
    """Đánh dấu công việc hoàn thành."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Đã hoàn thành công việc.")
    else:
        print("Chỉ số công việc không hợp lệ.")


def delete_task(task_index):
    """Xóa công việc."""
    if 0 <= task_index < len(tasks):
        deleted = tasks.pop(task_index)
        print(f"Đã xóa: {deleted['name']}")
    else:
        print("Chỉ số công việc không hợp lệ.")


if __name__ == "__main__":
    print("Chào mừng đến với To-Do List!")

    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    add_task("Ôn tập Python")

    list_tasks()

    complete_task(0)
    list_tasks()

    delete_task(1)
    list_tasks()
