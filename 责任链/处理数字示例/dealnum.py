"""
__author__ = jaxon
__time__ = 2023/8/30 19:19
__desc__ = ''
"""
from abc import ABC, abstractmethod


# --------------抽象处理者---------------
class AbcCheckHandler(ABC):

    @abstractmethod
    def check_password(self, password):
        pass

    @abstractmethod
    def set_next(self, handler):
        pass


# ---------------具体处理---------------
class CheckHanlderBase(AbcCheckHandler):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler

    @abstractmethod
    def _check(self, password):
        pass

    def check_password(self, password):
        status, msg = self._check(password)
        if status:
            if self._next_handler:
                return self._next_handler.check_password(password)
            else:
                return True, ''
        else:
            return status, msg


class LengthCheckHandler(CheckHanlderBase):
    """
    专门检查长度
    """

    def _check(self, password):
        if len(password) > 6:
            return True, ''
        return False, '长度错误'


class CaseCheckHandler(CheckHanlderBase):
    """
    专门检查大小写
    """

    def _check(self, password):
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
    def _check(self, password):
        for letter in ('!', '@', '#', '$'):
            if letter in password:
                return True, ''
        return False, '未包含特殊字符'


# ---------调用------------
def check_password(password):
    # 检查长度
    len_checker = LengthCheckHandler()
    # 检查大小写
    case_checker = CaseCheckHandler()
    # 检查特殊字符
    special_checker = SpecialCheckHandler()
    # 设置调用链
    # 检查长度> 检查大小写 > 检查特殊字符
    len_checker.set_next(case_checker)
    case_checker.set_next(special_checker)

    status, msg = len_checker.check_password(password)
    if status:
        print(f"{password} 检查通过")
    else:
        print(f"{password} 检查不通过: {msg}")


if __name__ == '__main__':
    check_password("aA1111111")
