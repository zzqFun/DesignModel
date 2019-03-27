# coding = utf-8
from simple_factory_model import operate


class Factory:
    def __init__(self, opt):
        self.opt = opt

    def switch(self):
        if self.opt == '+':
            return operate.OperateAdd()
        elif self.opt == '-':
            return operate.OperateSub()
        elif self.opt == '*':
            return operate.OperateMul()
        elif self.opt == '/':
            return operate.OperateDiv()
