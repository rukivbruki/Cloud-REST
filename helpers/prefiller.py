import shared


def prefill_stack(operations_name, task):
    if len(shared.operations) == 0:
        shared.operations.append({'command': operations_name, "task": "NO COMMANDS"})
        shared.operations.append({'command': operations_name, "task": "NO COMMANDS"})

    shared.operations.insert(1, {'command': operations_name, "task": [task]})
