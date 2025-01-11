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

date_ideas = ['Wine Farm date', 'Aquarium date', 'Dinner date', 'Chasing the sunset date', 'Fair date', 'Weekend away date',
              'Beach date', 'Picnic date', 'Game night date', 'Sip n Paint date', 'Stargazing date', 
              'Movie date', 'Outdoor adventure date', 'Art gallery date', 'Exploring restaurants date'
              , 'Road trip date']

date = random.choice(date_ideas)

print('\nSo there we have it. The date night idea for you two this time around is...')
print(f'Prepare to go on a {date.upper()}.')