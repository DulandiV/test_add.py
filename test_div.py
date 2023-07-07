import pytest

@pytest.mark.parametrize("num, output", [(2, 50), (5, 20), (10, 10), (4, 25)])
def test_division(num, output):
   assert 100 / num == output  
