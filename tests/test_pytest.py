import pytest
from main import solve

@pytest.mark.parametrize(
    'here,turtle,expected',
    (
        [[8, 5, 3, 2, 0, 1, 1], [3, 3, 3, 3, 3, 3, 3], 'черепаха'],
        [[8, 5, 3, 2, 2, 1, 1], [3, 3, 3, 3, 3, 3, 3], 'заяц'],
        [[8, 5, 3, 2, 1, 1, 1], [3, 3, 3, 3, 3, 3, 3], 'одинаково'],
    )
)
def test_solve(here, turtle, expected):
    actual = solve(here, turtle)
    assert expected == actual

