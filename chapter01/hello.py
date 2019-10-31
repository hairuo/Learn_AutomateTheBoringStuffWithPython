#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 22:12:47 2018
Learning a book named "Automate the boring stuff with python".
@author: cbg
"""

# Ths program says hello and asks for my name.


print('Hello world!')
print('What is your name?')  # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')  # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
