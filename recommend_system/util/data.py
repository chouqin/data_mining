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

class NetflixData(Data):
    def __init__(self, file_name, sep):
        super(NetflixData, self).__init__(file_name, sep)

    def loads():
        """
        read file contents, return RatingMatrix
        """
        pass

    def stats(self):
        pass

class MovielensData(Data):
    def __init__(self, file_name, sep):
        super(MovielensData, self).__init__(file_name, sep)

    def loads():
        """
        read file contents, return RatingMatrix
        """
        pass

    def stats(self):
        pass
