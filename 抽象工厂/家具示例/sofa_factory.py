"""
__author__ = 'jaxon'
__time__ = '2022/12/28 16:25'
__desc__ = ''
"""
from abc import ABCMeta, abstractmethod


class Sofa(metaclass=ABCMeta):
    @abstractmethod
    def create_art_deco(self):
        # 生产装饰风艺术的沙发
        ...

    @abstractmethod
    def create_victorian(self):
        # 生产维多利亚风格的沙发
        ...

    @abstractmethod
    def create_modern(self):
        # 生产现代风格的沙发
        ...
