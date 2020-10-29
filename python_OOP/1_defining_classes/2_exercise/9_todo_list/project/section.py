from typing import List
from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'
        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str):
        tasks_list = [t for t in self.tasks if t.name == task_name]
        if tasks_list:
            current_task = tasks_list[0]
            current_task.completed = True
            return f'Completed task {task_name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        completed_tasks = [t for t in self.tasks if t.completed]
        for c_t in completed_tasks:
            self.tasks.remove(c_t)
        return f'Cleared {len(completed_tasks)} tasks.'

    def view_section(self):
        section_name = f'Section {self.name}:\n'
        tasks_info = '\n'.join([t.details() for t in self.tasks])
        return section_name + tasks_info
