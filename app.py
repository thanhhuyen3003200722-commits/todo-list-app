
tasks = []

def add_task(task_name):
    tasks.append({
        "name": task_name,
        "completed": False
    })
    print(f"Da them cong viec: {task_name}")

def list_tasks():
    if not tasks:
        print("Danh sach cong viec dang trong.")
        return

    print("\nDanh sach cong viec:")
    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{index}. {status} {task['name']}")

def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"Da hoan thanh: {tasks[task_index]['name']}")
    else:
        print("Loi: Chi so cong viec khong hop le.")

def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Da xoa cong viec: {removed_task['name']}")
    else:
        print("Loi: Chi so cong viec khong hop le.")

if __name__ == "__main__":
    add_task("Hoc Git va GitHub")
    add_task("Lam bai tap thuc hanh")

    list_tasks()
    complete_task(0)
    list_tasks()

    delete_task(1)
    list_tasks()
