# coding=utf-8
# 上下文, 维护一个对strategy对象的引用,这个例子结合了简单工厂模式,再客户端隐藏了代码
from strategy_main import*


class Context:
    def __init__(self, model_type):
        self.__model_type = model_type
        if self.__model_type == "model1":
            self.__strategy = StrategyA()
        elif self.__model_type == "model2":
            self.__strategy = StrategyB()
        elif self.__model_type == "model3":
            self.__strategy = StrategyC()

    def do_calculate(self):
        return self.__strategy.calculate()
