from helpers import get_stack, update_stack


def prefill_stack(operations_name, task):
    operations = get_stack('operations')
    print(operations)
    if len(operations) == 0:
        operations.append({'command': operations_name, "task": "NO COMMANDS"})
        operations.append({'command': operations_name, "task": "NO COMMANDS"})
    operations.insert(1, {'command': operations_name, "task": task})

    update_stack("operations", operations)
