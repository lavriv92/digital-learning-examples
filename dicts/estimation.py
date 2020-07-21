from prettytable import PrettyTable

task_titles = [
  'Listen the course',
  'Ask questions if needs',
  'Complete home task',
  'Complete practical work'
]
tasks = [ {'title': title, 'estimate': 0} for title in task_titles ]


for task in tasks:
    skip = input(f"Put 'yes' if you want to skip {task['title']}: ")

    if skip == 'yes':
        continue
    else:
        estimate = float(input(f"Enter estimate of {task['title']}: "))
        task['estimate'] = estimate
    print('\n')


table = PrettyTable()
table.field_names = ['Title', 'Estimate']


# Print results of estimation
for task in tasks:
    table.add_row(task.values())

print(table)
