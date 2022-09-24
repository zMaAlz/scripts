#!/usr/bin/env python3
import os
path_repo=input("Укажите путь к репозиторию: ")
bash_command = [f"cd {path_repo}", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
print('Modified:')
for result in result_os.split('\n'):
    if result.find('modified') == 1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(path_repo+prepare_result)
print('New files:')
for result in result_os.split('\n'):
    if result.find('new file') == 1:
        new_result = result.replace('\tnew file:   ', '')
        print(path_repo+new_result)
        