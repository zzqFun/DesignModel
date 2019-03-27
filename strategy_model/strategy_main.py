# coding = utf-8
from strategy import Strategy

# 具体策略类, 封装了具体的算法和行为


class StrategyA(Strategy):

    def calculate(self):
        print("StrategyA")


class StrategyB(Strategy):

    def calculate(self):
        print("StrategyB")


class StrategyC(Strategy):

    def calculate(self):
        print("StrategyC")
