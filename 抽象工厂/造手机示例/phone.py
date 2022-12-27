"""
__author__ = 'jaxon'
__time__ = '2022/12/27 16:40'
__desc__ = ''
"""
from abc import ABCMeta, abstractmethod


class ProduceShell(metaclass=ABCMeta):
    @abstractmethod
    def produce_shell(self):
        """
        生产手机壳
        :return:
        """
        ...


class ProduceOS(metaclass=ABCMeta):
    @abstractmethod
    def produce_os(self):
        """
        生产手机系统
        :return:
        """
        ...


class ProduceCPU(metaclass=ABCMeta):
    @abstractmethod
    def produce_cpu(self):
        """
        生产cpu
        :return:
        """
        ...


