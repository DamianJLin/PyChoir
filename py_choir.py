import random
from src.tips import TIPS
from src.members import add_member

if __name__ == '__main__':
    print('Tip: ' + random.choice(TIPS))

    while True:
        command = input()
        match command.split():
            case ['members', 'view']:
                pass
            case ['members', 'add' | 'new']:
                add_member()
            case ['rolls', 'mark']:
                pass
            case ['rolls', 'view']:
                pass
            case ['rolls', 'eligibility']:
                pass
            case ['help', *args]:
                print('Commands:')
                print('members view\t\tview membership list')
                print('members add\t\t\tadd to membership list')
                print('rolls mark\t\t\tmark the roll')
                print('rolls view\t\t\tview marked rolls')
                print('rolls eligibility\ttools for checking chorister attendance')
            case _:
                print('Unrecognised command, type help for help.')
