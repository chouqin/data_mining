# -*- coding=utf-8 -*-

"""
data load model
two basic function:
    1. load data from files
    2. get data stats
"""

class Data:
    def __init__(self, file_name, sep):
        self.file_name = file_name
        self.sep = sep

    def loads(self):
        raise NotImplementedError

    def stats(self):
        raise NotImplementedError

class NetflixTrainData(Data):
    def loads():
        """
        read file contents, return RatingMatrix
        """
        pass

    def stats(self):
        pass

class NetflixTestData(Data):
    def loads():
        """
        read file contents, return a list of (uid, iid, rating)
        """
        pass

    def stats(self):
        pass

class MovielensTrainData(Data):
    def loads():
        """
        read file contents, return RatingMatrix
        """
        pass

    def stats(self):
        pass

class MovielensTestData(Data):
    def loads():
        """
        read file contents, return a list of (uid, iid, rating)
        """
        pass

    def stats(self):
        pass
