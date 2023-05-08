import pytest
from models import Calculator


def test_models_calculator():
    calc = Calculator()
    result = calc.add(1, 2)
    assert result == 3
    assert result == calc.last_result
