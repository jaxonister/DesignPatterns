"""
__author__ = jaxon
__time__ = 2023/8/31 16:33
__desc__ = ''
"""
from abc import ABC, abstractmethod


class AbcCheckHandler(ABC):

    @abstractmethod
    def check_password(self, data, password):
        pass

    @abstractmethod
    def is_deal(self, handler):
        ...


class CheckHanlderBase(AbcCheckHandler):
    _next_handler = None

    def is_deal(self, handler):
        ...

    def check_password(self, data: list, password):
        for x in data:
            status, msg = x.is_deal(password)
            if not status:
                return msg
            return status


class LengthCheckHandler(CheckHanlderBase):
    """
    专门检查长度
    """

    def is_deal(self, password):
        if len(password) > 6:
            return True, ''
        return False, '长度错误'


class CaseCheckHandler(CheckHanlderBase):
    """
    专门检查大小写
    """

    def is_deal(self, password):
        has_lower = False
        has_upper = False

        for letter in password:
            if 'a' <= letter <= 'z':
                has_lower = True
            if 'A' <= letter <= 'Z':
                has_upper = True

        if has_lower and has_upper:
            return True, ''
        else:
            return False, '大小写不符合要求'


class SpecialCheckHandler(CheckHanlderBase):
    def is_deal(self, password):
        for letter in ('!', '@', '#', '$'):
            if letter in password:
                return True, ''
        return False, '未包含特殊字符'


def check_password(password):
    # 检查长度
    len_checker = LengthCheckHandler()
    # 检查大小写
    case_checker = CaseCheckHandler()
    # 检查特殊字符
    special_checker = SpecialCheckHandler()
    ins = [len_checker, case_checker, special_checker]

    r = CheckHanlderBase().check_password(ins, password)
    return r


if __name__ == '__main__':
    check_password("aA111!1111")
