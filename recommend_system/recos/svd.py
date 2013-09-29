# -*- coding=utf-8 -*-

"""
implementation of the svd recommender
"""

from base import Recommender

class svd(Recommender):
    def init_parameters(self):
        raise NotImplementedError

    def train(self):
        raise NotImplementedError

    def test(self):
        raise NotImplementedError

