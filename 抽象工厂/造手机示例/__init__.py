"""
__author__ = 'jaxon'
__time__ = '2022/12/27 16:39'
__desc__ = ''
"""

"""
抽象工厂模式
生产一整套产品，让他们有自己的依赖关系。（结构要固定）
工厂指定一类产品，客户端可以更换新的工厂，生产新一类的产品。
但是产品的结构是固定的。否则整个代码都要修改。

例如：假定手机的结构，只能使用
CPU、手机壳、系统、三部分组成。（假定结构由三部分组成）
工厂生产不同类型的手机，系统可以有多种，CPU可以有多种，手机壳可以有多种。
可以拓展新手机，但是不能更改手机的 “三部分” 组成结构
"""
