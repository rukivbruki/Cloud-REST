from helpers import update_stack, get_stack


def clean_stack():
    operations = get_stack('operations')
    pointer = get_stack('pointer')
    first_task_index = 2
    if pointer > 1:
        del operations[first_task_index:pointer + 1]
        update_stack('operations', operations)

    update_stack('pointer', 1)
