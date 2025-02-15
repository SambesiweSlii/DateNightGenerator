# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:01:08 2025

@author: SambesiweSli
"""

# This Python program is designed to generate a date night
# it is tricky deciding on what to do so this will help with deciding.
# it will contain a list of predetermined date ideas that are chosen by myself
# and my girlfriend
import random

print("It's that time again. DATE NIGHT TIME!")
print("Let's see what date night idea is in store for you today.")

# this list holds the date ideas...
# we can add and remove contents within the list.
date_ideas = ['Wine Farm date', 'Aquarium date', 'Dinner date', 'Chasing the sunset date', 'Arcade date', 'Bowling date', 'Fair date', 'Weekend away date',
              'Beach date', 'Picnic date', 'Game night date', 'Sip n Paint date', 'Stargazing date', 
              'Movie date', 'Art gallery date', 'Exploring restaurants date', 'Farmers Market date'
              , 'Road trip date', 'Ziplining date', 'Quad bike date', 'Paintball shooting date', 'Painting and Pottery date']

# the date variable will hold the randomly generated date idea
date = random.choice(date_ideas)

# okay, so here we are printing what we need to see...
# which is a date idea and some additional text not to make it look boring.
print('\nSo there we have it. The date night idea for you two this time around is...')
print(f'Prepare to go on a {date.upper()}.')

# the intention now is to prompt the user if they are happy with...
# the idea generated to them or would they like to go again.
print('\nAre you happy with this or would you like to go again?')
answer = str(input('Yes? / No? : '))
print('\n')

# once we have the answer then we progress from the...
# if the answer is yes, the aim is to generate another date idea and print it.
# else print the original generated date idea showing them it has stayed the same
if answer == 'Yes' or answer == 'yes':
    print(f'You answered {answer}.')
    print(random.choice(date_ideas))
    
    while answer == 'Yes' or answer == 'yes':
        print('\nAre you happy with this or would you like to go again?')
        answer = str(input('Yes? / No? : '))
        if answer == 'Yes' or answer == 'yes':
            random_date = random.choice(date_ideas)
            print(f'You answered {answer}.')
            print(random_date)
        elif answer == 'No' or answer == 'no': 
            print(f'You answered {answer}.')
            print(f'{random_date.upper()} it is then.')
            
elif answer == 'No' or answer == 'no': 
    print(f'You answered {answer}.')
    print(f'{date.upper()} it is then.')