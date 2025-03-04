import pytest
from src import calculator

def test_add():
    assert calculator.add(1,2) == 3
    assert calculator.add(0,5) == 5
    assert calculator.add(-2,9) == 7
    assert calculator.add(5,-8) == -3
    
@pytest.mark.parametrize( "a,b, expected",
    [
        (1,2,3),
        (0,5,5),
        (-2,9,7),
        (5,-8,-3),
    ]
)
def test_add_parametrized(a, b, expected):
    assert calculator.add(a,b) == expected
    
def test_add_2():
    assert calculator.add_wrong(1,2) == 3
    assert calculator.add_wrong(0,5) == 5
    assert calculator.add_wrong(-2,9) == 7
    assert calculator.add_wrong(5,-8) == -3
    

@pytest.mark.parametrize( "x,y, expected",
    [
        (1,2,3),
        (0,5,5),
        (-2,9,7),
        (5,-8,-3),
    ]
)
def test_add_wrong_parametrized(x, y, expected):
    assert calculator.add_wrong(x,y) == expected