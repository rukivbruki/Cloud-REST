import shared


def clean_stack():
    first_task_index = 2
    if shared.pointer > 1:
        del shared.operations[first_task_index:shared.pointer + 1]

    shared.pointer = 1
