import cube
import pytest

cubes = (
    (0 ,0),
    (1, 1),
    (2, 8),
    (3, 27)
)

@pytest.mark.parametrize('n, expected', cubes)
def test_cube(n, expected):
    assert cube.cube(n) == expected

def test_no_arguments():
    with pytest.raises(TypeError):
        cube.cube()

def test_exception_str():
    with pytest.raises(TypeError):
        cube.cube('x')

cube_roots = (
    (0, 0),
    (1, 1),
    (8, 2),
    (27, 3),
)

@pytest.mark.parametrize('n, expected', cube_roots)
def test_cube_root(n, expected):
    assert cube.cube_root(n) == expected

def test_cube_root_below_zero():
    with pytest.raises(ValueError):
        cube.cube_root(-1)
