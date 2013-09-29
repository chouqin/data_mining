# -*- coding=utf-8 -*-

from os import listdir
from os.path import join

# traverse directory, get all documents:
def traverse_directory(directory):
    for f in listdir(directory):
        yield join(directory, f)
