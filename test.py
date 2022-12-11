# test the functionally of the solver by comparing the output of the solver with the solved cube
from rubix_cube import RubixCube

rubix_cube = RubixCube(n=3)
rubix_cube.print_cube()

# test cases
def test_is_solved():
    assert rubix_cube.is_solved() == 0
    # rubix_cube.solve()
    assert rubix_cube.is_solved() == 0
    
test_is_solved()
