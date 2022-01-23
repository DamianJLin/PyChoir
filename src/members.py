from pathlib import Path

import numpy as np
import pandas as pd
from datetime import date

data_path = Path(__file__).parent.parent / 'data'
member_db_path = data_path / 'members.csv'


def add_member():

    # Open database file. TODO: Error handling properly.
    try:
        old_members = pd.read_csv(member_db_path, index_col=0)
    except FileNotFoundError:
        raise Exception('Cannot find members.csv.')

    # First Name
    first_name = input('First Name: ')\
        .lstrip().rstrip()

    # Last Name
    last_name = input('Last Name: ')\
        .lstrip().rstrip()

    # Vocal Part
    vocal_part = None
    while vocal_part not in {'Soprano', 'Alto', 'Tenor', 'Bass'}:
        vocal_part = input('Vocal Part (Soprano/Alto/Tenor/Bass): ')\
            .lstrip().rstrip().capitalize()

        if vocal_part == 'S':
            vocal_part = 'Soprano'
        if vocal_part == 'A':
            vocal_part = 'Alto'
        if vocal_part == 'T':
            vocal_part = 'Tenor'
        if vocal_part == 'B':
            vocal_part = 'Bass'

        if vocal_part not in {'Soprano', 'Alto', 'Tenor', 'Bass'}:
            print('Please enter SATB vocal part.')

    assert vocal_part in {'Soprano', 'Alto', 'Tenor', 'Bass'}

    # USU Number
    usu_number = None
    while usu_number is None:
        usu_number = input('USU Number (leave blank for none): ')\
            .lstrip().rstrip()

        try:
            usu_number = abs(int(usu_number))
        except ValueError:
            usu_number = None
            print('Please enter a valid USU number.')

    assert isinstance(usu_number, int) or np.isnan(usu_number)

    # Join Date
    join_date = date.today().isoformat()

    new_member = pd.DataFrame(
        {
            'first_name': [first_name],
            'last_name': [last_name],
            'vocal_part': [vocal_part],
            'usu_number': [usu_number],
            'join_date': [join_date],
         }
    )

    # Check duplicates
    dupe_array = (
        old_members['first_name'] == first_name
    )
    if any(dupe_array):
        print('Warning! Possible duplicate entries found:')
        print(old_members[dupe_array].to_string(index=False, justify='left'))

    # Confirmation
    confirmation = None
    print('Confirm new entry to database:')
    print(new_member.to_string(index=False, justify='left'))

    while confirmation is None:
        confirmation = input().lower()

        if confirmation in {'', 'y', 'yes'}:
            confirmation = True

        elif confirmation in {'n', 'no'}:
            print('Aborting member creation.')
            confirmation = False

        else:
            print('y or n')
            confirmation = None

    # Write to csv
    if confirmation:
        new_member.to_csv(member_db_path, mode='a', header=False)
