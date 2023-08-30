"""
__author__ = 'jaxon'
__time__ = '2022/12/27 17:21'
__desc__ = '抽象工厂'
"""
# 定义产品的描述、规范
from abc import ABCMeta, abstractmethod


class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def produce_shell(self):
        ...

    @abstractmethod
    def product_CPU(self):
        ...

    @abstractmethod
    def product_OS(self):
        ...
