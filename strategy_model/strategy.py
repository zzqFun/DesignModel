# coding = utf-8
from abc import ABCMeta, abstractmethod

# 策略类, 定义所有支持的算法的公共接口


class Strategy(metaclass=ABCMeta):

    @abstractmethod
    def calculate(self):
        pass


