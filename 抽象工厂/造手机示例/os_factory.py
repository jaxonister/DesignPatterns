"""
__author__ = 'jaxon'
__time__ = '2022/12/27 17:14'
__desc__ = ''
"""
from 抽象工厂.造手机示例.phone import ProduceOS


class AppleOS(ProduceOS):
    def produce_os(self):
        """
        生产 apple os
        :return:
        """
        print("Apple os")


class AndroidOS(ProduceOS):
    def produce_os(self):
        """
        生产 Android os
        :return:
        """
        print("Android os")
