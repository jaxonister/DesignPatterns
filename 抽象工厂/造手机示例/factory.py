"""
__author__ = 'jaxon'
__time__ = '2022/12/27 17:36'
__desc__ = '具体工厂实现'
"""
from 抽象工厂.造手机示例.cpu_factory import ArmCPU, X86CPU
from 抽象工厂.造手机示例.os_factory import AppleOS, AndroidOS
from 抽象工厂.造手机示例.phone_factory import PhoneFactory
from 抽象工厂.造手机示例.shell_factory import RedShell


class AppleFactory(PhoneFactory):
    def produce_shell(self):
        return RedShell()

    def product_CPU(self):
        return ArmCPU()

    def product_OS(self):
        return AppleOS()


class XiaoMiFactory(PhoneFactory):
    def produce_shell(self):
        return RedShell()

    def product_CPU(self):
        return X86CPU()

    def product_OS(self):
        return AndroidOS()
