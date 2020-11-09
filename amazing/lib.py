# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for amazing Project
"""

import os

def try_me():
    if os.getlogin():
        print(f'{os.getlogin()}, you are amazing!!')
    else:
        print('this is amazing!!')


if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
    try_me()

