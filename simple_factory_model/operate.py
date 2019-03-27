# coding = utf-8
from simple_factory_model import operate_main


class OperateAdd(operate_main.OperateMain):
    def result(self):
        results = self.number_a + self.number_b
        return results


class OperateSub(operate_main.OperateMain):
    def result(self):
        results = self.number_a - self.number_b
        return results


class OperateMul(operate_main.OperateMain):
    def result(self):
        results = self.number_a * self.number_b
        return results


class OperateDiv(operate_main.OperateMain):
    def result(self):
        if self.number_b == 0:
            raise Exception("输入有误")
        results = self.number_a / self.number_b
        return results
