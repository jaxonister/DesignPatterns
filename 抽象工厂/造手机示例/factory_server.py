"""
__author__ = 'jaxon'
__time__ = '2022/12/27 17:51'
__desc__ = ''
"""
from 抽象工厂.造手机示例.factory import AppleFactory


class Phone:
    def __init__(self, shell, cpu, os):
        self.shell = shell
        self.cpu = cpu
        self.os = os

    def show_info(self):
        print('手机信息：')
        self.shell.produce_shell()
        self.cpu.produce_cpu()
        self.os.produce_os()


def make_phone(factory):
    shell = factory.produce_shell()
    cpu = factory.product_CPU()
    os = factory.product_OS()
    return Phone(shell, cpu, os)


if __name__ == '__main__':
    p = make_phone(AppleFactory())
    p.show_info()
