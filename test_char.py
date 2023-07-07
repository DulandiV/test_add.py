import pytest

@pytest.mark.parametrize("char, output", [('a', 'az'), ('b', 'bz'), ('c', 'cz'), ('d', 'dz')])
def test_character_and_string_operations(char, output):

#conca
    assert char + 'z' == output  # Concatenation
    assert output.startswith(char)  # StartsWith
    assert output.endswith('z')  # EndsWith






