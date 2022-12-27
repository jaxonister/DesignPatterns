"""
__author__ = 'jaxon'
__time__ = '2022/12/27 17:07'
__desc__ = ''
"""

from 抽象工厂.造手机示例.phone import ProduceShell


class RedShell(ProduceShell):
    def produce_shell(self):
        """
        造红色手机壳
        :return:
        """
        print("红色手机壳")


class VioletShell(ProduceShell):
    def produce_shell(self):
        """
        造紫色手机壳
        :return:
        """
        print("红色手机壳")
