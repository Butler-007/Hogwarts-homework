# coding:utf-8
# author:Lijian time:2020/12/28
import pytest
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a, b, expect", [(3, 5, 8), (-1, -5, -6), (100, 357, 457)
                                              ], ids=("int", "minus", "bigint"))
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a, b, expect", [(3, 5, -2), (-6, -4, -2), (300, 100, 200)
                                              ], ids=("int", "minus", "bigint"))
    def test_sub(self, a, b, expect):
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a, b, expect", [(3, 5, 15), (-2, -4, 8), (300, 100, 30000)
                                              ], ids=("int", "minus", "bigint"))
    def test_mul(self, a, b, expect):
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a, b, expect", [(15, 3, 5), (-2, -4, 0.5), (200, 100, 2)
                                              ], ids=("int", "minus", "bigint"))
    def test_div(self, a, b, expect):
        assert expect == self.calc.div(a, b)
