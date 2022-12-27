"""
__author__ = 'jaxon'
__time__ = '2022/12/27 17:12'
__desc__ = ''
"""
from 抽象工厂.造手机示例.phone import ProduceCPU


class X86CPU(ProduceCPU):
    def produce_cpu(self):
        """
        生产x86 cpu
        :return:
        """
        print("x86 cpu")


class ArmCPU(ProduceCPU):
    def produce_cpu(self):
        """
        生产arm cpu
        :return:
        """
        print("arm cpu")
