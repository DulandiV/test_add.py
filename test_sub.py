import pytest

@pytest.mark.parametrize("num, output",[(1,12),(2,13),(3,14),(4,15)])
def test_substraction(num, output):
   assert output-num == 11
