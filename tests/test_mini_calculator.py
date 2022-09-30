from assertpy import assert_that, soft_assertions
from mini_calculator import MiniCalculator


def test_sum():
    mini_calculator = MiniCalculator()
    with soft_assertions():
        assert_that(mini_calculator.sum(5, 6)).is_equal_to(11)
        assert_that(mini_calculator.sum(5, 5)).is_equal_to(10)
        assert_that(mini_calculator.sum(-5, 5)).is_equal_to(0)


def test_diff():
    mini_calculator = MiniCalculator()
    with soft_assertions():
        assert_that(mini_calculator.diff(15, 6)).is_equal_to(9)
        assert_that(mini_calculator.diff(0, 5)).is_equal_to(-5)
        assert_that(mini_calculator.diff(-5, 5)).is_equal_to(-10)


def test_inmultire():
    mini_calculator = MiniCalculator()
    with soft_assertions():
        assert_that(mini_calculator.inmultire(2, 6)).is_equal_to(12)
        assert_that(mini_calculator.inmultire(1, 5)).is_equal_to(5)
        assert_that(mini_calculator.inmultire(-5, 5)).is_equal_to(-25)


def test_impartire():
    mini_calculator = MiniCalculator()
    with soft_assertions():
        assert_that(mini_calculator.impartire(6, 6)).is_equal_to(1)
        assert_that(mini_calculator.impartire(10, 5)).is_equal_to(2)
        assert_that(mini_calculator.impartire(-55, 5)).is_equal_to(-11)
