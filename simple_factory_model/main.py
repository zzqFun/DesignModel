# coding = utf-8
from simple_factory_model import factory

operate = factory.Factory('+').switch()
operate.number_a = 3
operate.number_b = 4
print(operate.result())
