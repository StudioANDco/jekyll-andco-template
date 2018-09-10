#!/usr/bin/env python

import os


if __name__ == '__main__':
    os.system('git init .')
    os.system('pre-commit install')
    os.system('npm install')
    os.system('node_modules/.bin/kanbasu _sass/')
    os.system('git add .')
    os.system('git add -f node_modules/kanbasu/src/scss/')
    os.system('git commit -am "first blood"')
