import math

import numpy as np
import torch
from numpy import ndarray
from torch import Tensor

import koila
from koila import LazyTensor

from . import common


def scalar_isclose(a: float, b: float) -> None:
    assert math.isclose(a, b, abs_tol=1e-5), [a, b]


def tensor_allclose(a: Tensor, b: Tensor) -> None:
    assert a.allclose(b, atol=1e-5), a != b


def array_allclose(a: ndarray, b: ndarray) -> None:
    assert np.allclose(a, b, atol=1e-5), a != b


def test_scalar_positive_op() -> None:
    common.call(
        lambda a, c: scalar_isclose((+a).item(), c),
        [[LazyTensor(torch.tensor(-11)), -11]],
    )


def test_scalar_positive_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.positive().item(), c),
        [[LazyTensor(torch.tensor(4)), 4]],
    )


def test_scalar_positive_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.positive(a).item(), c),
        [[LazyTensor(torch.tensor(-8)), -8]],
    )


def test_scalar_negative_op() -> None:
    common.call(
        lambda a, c: scalar_isclose((-a).item(), c),
        [[LazyTensor(torch.tensor(-13)), 13]],
    )


def test_scalar_negative_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.neg().item(), c),
        [[LazyTensor(torch.tensor(2)), -2]],
    )


def test_scalar_negative_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.neg(a).item(), c),
        [[LazyTensor(torch.tensor(-5)), 5]],
    )


def test_scalar_add_op() -> None:
    common.call(
        lambda a, b, c: scalar_isclose((a + b).item(), c),
        [
            [LazyTensor(torch.tensor(1)), LazyTensor(torch.tensor(2)), 1 + 2],
            [torch.tensor(1), LazyTensor(torch.tensor(2)), 1 + 2],
            [LazyTensor(torch.tensor(1)), torch.tensor(2), 1 + 2],
        ],
    )


def test_scalar_add_method() -> None:
    common.call(
        lambda a, b, c: scalar_isclose(a.add(b).item(), c),
        [
            [LazyTensor(torch.tensor(4)), LazyTensor(torch.tensor(3)), 4 + 3],
            [torch.tensor(4), LazyTensor(torch.tensor(3)), 4 + 3],
            [LazyTensor(torch.tensor(4)), torch.tensor(3), 4 + 3],
        ],
    )


def test_scalar_add_function() -> None:
    common.call(
        lambda a, b, c: scalar_isclose(torch.add(a, b).item(), c),
        [
            [LazyTensor(torch.tensor(8)), LazyTensor(torch.tensor(4)), 8 + 4],
            [torch.tensor(8), LazyTensor(torch.tensor(4)), 8 + 4],
            [LazyTensor(torch.tensor(8)), torch.tensor(4), 8 + 4],
        ],
    )


def test_scalar_sub_op() -> None:
    common.call(
        lambda a, b, c: scalar_isclose((a - b).item(), c),
        [
            [LazyTensor(torch.tensor(1)), LazyTensor(torch.tensor(2)), 1 - 2],
            [torch.tensor(1), LazyTensor(torch.tensor(2)), 1 - 2],
            [LazyTensor(torch.tensor(1)), torch.tensor(2), 1 - 2],
        ],
    )


def test_scalar_sub_method() -> None:
    common.call(
        lambda a, b, c: scalar_isclose(a.sub(b).item(), c),
        [
            [LazyTensor(torch.tensor(4)), LazyTensor(torch.tensor(3)), 4 - 3],
            [torch.tensor(4), LazyTensor(torch.tensor(3)), 4 - 3],
            [LazyTensor(torch.tensor(4)), torch.tensor(3), 4 - 3],
        ],
    )


def test_scalar_sub_function() -> None:
    common.call(
        lambda a, b, c: scalar_isclose(torch.sub(a, b).item(), c),
        [
            [LazyTensor(torch.tensor(8)), LazyTensor(torch.tensor(4)), 8 - 4],
            [torch.tensor(8), LazyTensor(torch.tensor(4)), 8 - 4],
            [LazyTensor(torch.tensor(8)), torch.tensor(4), 8 - 4],
        ],
    )


def test_scalar_mul_op() -> None:
    common.call(
        lambda a, b, c: scalar_isclose((a * b).item(), c),
        [
            [LazyTensor(torch.tensor(0.5)), LazyTensor(torch.tensor(2)), 0.5 * 2],
            [torch.tensor(0.5), LazyTensor(torch.tensor(2)), 0.5 * 2],
            [LazyTensor(torch.tensor(0.5)), torch.tensor(2), 0.5 * 2],
        ],
    )


def test_scalar_mul_method() -> None:
    common.call(
        lambda a, b, c: scalar_isclose(a.mul(b).item(), c),
        [
            [LazyTensor(torch.tensor(4)), LazyTensor(torch.tensor(3)), 12],
            [torch.tensor(4), LazyTensor(torch.tensor(3)), 12],
            [LazyTensor(torch.tensor(4)), torch.tensor(3), 12],
        ],
    )


def test_scalar_mul_function() -> None:
    common.call(
        lambda a, b, c: scalar_isclose(torch.mul(a, b).item(), c),
        [
            [LazyTensor(torch.tensor(8)), LazyTensor(torch.tensor(4)), 32],
            [torch.tensor(8), LazyTensor(torch.tensor(4)), 32],
            [LazyTensor(torch.tensor(8)), torch.tensor(4), 32],
        ],
    )


def test_scalar_floordiv_op() -> None:
    common.call(
        common.is_notimplemented,
        [
            [lambda: LazyTensor(torch.tensor(1)) // LazyTensor(torch.tensor(2))],
            [lambda: torch.tensor(1) // LazyTensor(torch.tensor(2))],
            [lambda: LazyTensor(torch.tensor(1)) // torch.tensor(2)],
        ],
    )


def test_scalar_floordiv_method() -> None:
    common.call(
        lambda a, b, c: scalar_isclose(a.div(b, rounding_mode="trunc").item(), c),
        [
            [LazyTensor(torch.tensor(4)), LazyTensor(torch.tensor(3)), 4 // 3],
            [torch.tensor(4), LazyTensor(torch.tensor(3)), 4 // 3],
            [LazyTensor(torch.tensor(4)), torch.tensor(3), 4 // 3],
        ],
    )


def test_scalar_floordiv_function() -> None:
    common.call(
        lambda a, b, c: scalar_isclose(
            torch.div(a, b, rounding_mode="trunc").item(), c
        ),
        [
            [LazyTensor(torch.tensor(9)), LazyTensor(torch.tensor(4)), 9 // 4],
            [torch.tensor(9), LazyTensor(torch.tensor(4)), 9 // 4],
            [LazyTensor(torch.tensor(9)), torch.tensor(4), 9 // 4],
        ],
    )


def test_scalar_truediv_op() -> None:
    common.call(
        lambda a, b, c: scalar_isclose((a / b).item(), c),
        [
            [LazyTensor(torch.tensor(1)), LazyTensor(torch.tensor(2)), 1 / 2],
            [torch.tensor(1), LazyTensor(torch.tensor(2)), 1 / 2],
            [LazyTensor(torch.tensor(1)), torch.tensor(2), 1 / 2],
        ],
    )


def test_scalar_truediv_method() -> None:
    common.call(
        lambda a, b, c: scalar_isclose(a.div(b).item(), c),
        [
            [LazyTensor(torch.tensor(4)), LazyTensor(torch.tensor(3)), 4 / 3],
            [torch.tensor(4), LazyTensor(torch.tensor(3)), 4 / 3],
            [LazyTensor(torch.tensor(4)), torch.tensor(3), 4 / 3],
        ],
    )


def test_scalar_truediv_function() -> None:
    common.call(
        lambda a, b, c: scalar_isclose(torch.div(a, b).item(), c),
        [
            [LazyTensor(torch.tensor(9)), LazyTensor(torch.tensor(4)), 9 / 4],
            [torch.tensor(9), LazyTensor(torch.tensor(4)), 9 / 4],
            [LazyTensor(torch.tensor(9)), torch.tensor(4), 9 / 4],
        ],
    )


def test_scalar_pow_op() -> None:
    common.call(
        lambda a, b, c: scalar_isclose((a ** b).item(), c),
        [
            [LazyTensor(torch.tensor(1.5)), LazyTensor(torch.tensor(2)), 1.5 ** 2],
            [torch.tensor(1.5), LazyTensor(torch.tensor(2)), 1.5 ** 2],
            [LazyTensor(torch.tensor(1.5)), torch.tensor(2), 1.5 ** 2],
        ],
    )


def test_scalar_pow_method() -> None:
    common.call(
        lambda a, b, c: scalar_isclose(a.pow(b).item(), c),
        [
            [LazyTensor(torch.tensor(4)), LazyTensor(torch.tensor(3)), 4 ** 3],
            [torch.tensor(4), LazyTensor(torch.tensor(3)), 4 ** 3],
            [LazyTensor(torch.tensor(4)), torch.tensor(3), 4 ** 3],
        ],
    )


def test_scalar_pow_function() -> None:
    common.call(
        lambda a, b, c: scalar_isclose(torch.pow(a, b).item(), c),
        [
            [LazyTensor(torch.tensor(9.0)), LazyTensor(torch.tensor(-2)), 9.0 ** -2],
            [torch.tensor(9.0), LazyTensor(torch.tensor(-2)), 9.0 ** -2],
            [LazyTensor(torch.tensor(9.0)), torch.tensor(-2), 9.0 ** -2],
        ],
    )


def test_scalar_remainder_op() -> None:
    common.call(
        lambda a, b, c: scalar_isclose((a % b).item(), c),
        [
            [LazyTensor(torch.tensor(3.3)), LazyTensor(torch.tensor(1.9)), 3.3 % 1.9],
            [torch.tensor(3.3), LazyTensor(torch.tensor(1.9)), 3.3 % 1.9],
            [LazyTensor(torch.tensor(3.3)), torch.tensor(1.9), 3.3 % 1.9],
        ],
    )


def test_scalar_remainder_method() -> None:
    common.call(
        lambda a, b, c: scalar_isclose(a.remainder(b).item(), c),
        [
            [LazyTensor(torch.tensor(99)), LazyTensor(torch.tensor(7)), 99 % 7],
            [torch.tensor(99), LazyTensor(torch.tensor(7)), 99 % 7],
            [LazyTensor(torch.tensor(99)), torch.tensor(7), 99 % 7],
        ],
    )


def test_scalar_remainder_function() -> None:
    common.call(
        lambda a, b, c: scalar_isclose(torch.remainder(a, b).item(), c),
        [
            [LazyTensor(torch.tensor(25)), LazyTensor(torch.tensor(7.8)), 25 % 7.8],
            [torch.tensor(25), LazyTensor(torch.tensor(7.8)), 25 % 7.8],
            [LazyTensor(torch.tensor(25)), torch.tensor(7.8), 25 % 7.8],
        ],
    )


def test_matmul_op() -> None:
    arr = torch.randn(2, 10, 11)

    common.call(
        lambda a, b, c: tensor_allclose(koila.run(a @ b), c),
        [
            [LazyTensor(arr[0]), LazyTensor(arr[1].T), arr[0] @ arr[1].T],
            [arr[0], LazyTensor(arr[1].T), arr[0] @ arr[1].T],
            [LazyTensor(arr[0]), arr[1].T, arr[0] @ arr[1].T],
        ],
    )


def test_matmul_method() -> None:
    arr = torch.randn(2, 10, 11)

    common.call(
        lambda a, b, c: tensor_allclose(koila.run(a.matmul(b)), c),
        [
            [LazyTensor(arr[0]), LazyTensor(arr[1].T), arr[0] @ arr[1].T],
            [arr[0], LazyTensor(arr[1].T), arr[0] @ arr[1].T],
            [LazyTensor(arr[0]), arr[1].T, arr[0] @ arr[1].T],
        ],
    )


def test_matmul_function() -> None:
    arr = torch.randn(2, 10, 11)

    common.call(
        lambda a, b, c: tensor_allclose(koila.run(torch.matmul(a, b)), c),
        [
            [LazyTensor(arr[0]), LazyTensor(arr[1].T), arr[0] @ arr[1].T],
            [arr[0], LazyTensor(arr[1].T), arr[0] @ arr[1].T],
            [LazyTensor(arr[0]), arr[1].T, arr[0] @ arr[1].T],
        ],
    )


def test_scalar_identity() -> None:
    tensor = torch.tensor(13.5)

    assert LazyTensor(tensor).run() == 13.5
    assert LazyTensor(tensor).item() == 13.5
    assert int(LazyTensor(tensor)) == 13
    assert float(LazyTensor(tensor)) == 13.5
    assert bool(LazyTensor(tensor))

    tensor = torch.tensor(-17.5)
    assert LazyTensor(tensor).run() == -17.5
    assert LazyTensor(tensor).item() == -17.5
    assert int(LazyTensor(tensor)) == -17
    assert float(LazyTensor(tensor)) == -17.5
    assert bool(LazyTensor(tensor))

    tensor = torch.tensor(0)
    assert not LazyTensor(tensor).run()
    assert not LazyTensor(tensor).item()
    assert not int(LazyTensor(tensor))
    assert not float(LazyTensor(tensor))
    assert not bool(LazyTensor(tensor))


def test_scalar_frac_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.frac().item(), c),
        [
            [LazyTensor(torch.tensor(13.22)), 0.22],
            [LazyTensor(torch.tensor(55.0)), 0],
            [LazyTensor(torch.tensor(-55.55)), -0.55],
        ],
    )


def test_scalar_frac_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.frac(a).item(), c),
        [
            [LazyTensor(torch.tensor(25.25)), 0.25],
            [LazyTensor(torch.tensor(11.0)), 0],
            [LazyTensor(torch.tensor(-25.33)), -0.33],
        ],
    )


def test_scalar_exp_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.exp().item(), c),
        [
            [LazyTensor(torch.tensor(1.23)), math.e ** 1.23],
            [LazyTensor(torch.tensor(0)), 1],
            [LazyTensor(torch.tensor(1)), math.e],
        ],
    )


def test_scalar_exp_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.exp(a).item(), c),
        [
            [LazyTensor(torch.tensor(0.41)), math.e ** 0.41],
            [LazyTensor(torch.tensor(0)), 1],
            [LazyTensor(torch.tensor(1)), math.e],
        ],
    )


def test_scalar_exp2_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.exp2().item(), c),
        [
            [LazyTensor(torch.tensor(10)), 2 ** 10],
            [LazyTensor(torch.tensor(0)), 1],
            [LazyTensor(torch.tensor(1)), 2],
        ],
    )


def test_scalar_exp2_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.exp2(a).item(), c),
        [
            [LazyTensor(torch.tensor(-5)), 2 ** -5],
            [LazyTensor(torch.tensor(0)), 1],
            [LazyTensor(torch.tensor(1)), 2],
        ],
    )


def test_scalar_log_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.log().item(), c),
        [
            [LazyTensor(torch.tensor(13)), math.log(13)],
            [LazyTensor(torch.tensor(1)), 0],
            [LazyTensor(torch.tensor(math.e)), 1],
        ],
    )


def test_scalar_log_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.log(a).item(), c),
        [
            [LazyTensor(torch.tensor(5)), math.log(5)],
            [LazyTensor(torch.tensor(1)), 0],
            [LazyTensor(torch.tensor(math.e)), 1],
        ],
    )


def test_scalar_log2_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.log2().item(), c),
        [
            [LazyTensor(torch.tensor(442)), math.log2(442)],
            [LazyTensor(torch.tensor(1)), 0],
            [LazyTensor(torch.tensor(2)), 1],
        ],
    )


def test_scalar_log2_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.log2(a).item(), c),
        [
            [LazyTensor(torch.tensor(81)), math.log2(81)],
            [LazyTensor(torch.tensor(1)), 0],
            [LazyTensor(torch.tensor(2)), 1],
        ],
    )


def test_scalar_log10_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.log10().item(), c),
        [
            [LazyTensor(torch.tensor(132)), math.log10(132)],
            [LazyTensor(torch.tensor(1)), 0],
            [LazyTensor(torch.tensor(10)), 1],
        ],
    )


def test_scalar_log10_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.log10(a).item(), c),
        [
            [LazyTensor(torch.tensor(979)), math.log10(979)],
            [LazyTensor(torch.tensor(1)), 0],
            [LazyTensor(torch.tensor(10)), 1],
        ],
    )


def test_scalar_log1p_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.log1p().item(), c),
        [[LazyTensor(torch.tensor(1.5)), math.log1p(1.5)]],
    )


def test_scalar_log1p_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.log1p(a).item(), c),
        [[LazyTensor(torch.tensor(2.7)), math.log1p(2.7)]],
    )


def test_scalar_abs_op() -> None:
    common.call(
        lambda a, c: scalar_isclose(abs(a).item(), c),
        [
            [LazyTensor(torch.tensor(-7.122)), abs(-7.122)],
            [LazyTensor(torch.tensor(4.002)), abs(4.002)],
        ],
    )


def test_scalar_abs_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.abs().item(), c),
        [
            [LazyTensor(torch.tensor(-1.5)), abs(-1.5)],
            [LazyTensor(torch.tensor(3.7)), abs(3.7)],
        ],
    )


def test_scalar_abs_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.abs(a).item(), c),
        [
            [LazyTensor(torch.tensor(0.001)), abs(0.001)],
            [LazyTensor(torch.tensor(-24)), abs(-24)],
        ],
    )


def test_hash_op() -> None:
    arr = torch.randn(2, 10, 11)

    common.call(lambda a, c: koila.run(hash(a)) == hash(c), [[LazyTensor(arr), arr]])


def test_scalar_sin_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.sin().item(), c),
        [
            [LazyTensor(torch.tensor(0)), 0],
            [LazyTensor(torch.tensor(math.pi)), 0],
            [LazyTensor(torch.tensor(math.pi / 2)), 1],
            [LazyTensor(torch.tensor(3 * math.pi / 2)), -1],
            [LazyTensor(torch.tensor(42.0)), math.sin(42)],
            [LazyTensor(torch.tensor(-75.0)), math.sin(-75)],
        ],
    )


def test_scalar_sin_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.sin(a).item(), c),
        [
            [LazyTensor(torch.tensor(0)), 0],
            [LazyTensor(torch.tensor(math.pi)), 0],
            [LazyTensor(torch.tensor(math.pi / 2)), 1],
            [LazyTensor(torch.tensor(3 * math.pi / 2)), -1],
            [LazyTensor(torch.tensor(42.0)), math.sin(42)],
            [LazyTensor(torch.tensor(-75.0)), math.sin(-75)],
        ],
    )


def test_scalar_cos_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.cos().item(), c),
        [
            [LazyTensor(torch.tensor(0)), 1],
            [LazyTensor(torch.tensor(math.pi)), -1],
            [LazyTensor(torch.tensor(math.pi / 2)), 0],
            [LazyTensor(torch.tensor(3 * math.pi / 2)), 0],
            [LazyTensor(torch.tensor(27.0)), math.cos(27)],
            [LazyTensor(torch.tensor(-14.0)), math.cos(-14)],
        ],
    )


def test_scalar_cos_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.cos(a).item(), c),
        [
            [LazyTensor(torch.tensor(0)), 1],
            [LazyTensor(torch.tensor(math.pi)), -1],
            [LazyTensor(torch.tensor(math.pi / 2)), 0],
            [LazyTensor(torch.tensor(3 * math.pi / 2)), 0],
            [LazyTensor(torch.tensor(27.0)), math.cos(27)],
            [LazyTensor(torch.tensor(-14.0)), math.cos(-14)],
        ],
    )


def test_scalar_tan_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.tan().item(), c),
        [
            [LazyTensor(torch.tensor(0)), 0],
            [LazyTensor(torch.tensor(math.pi)), 0],
            [LazyTensor(torch.tensor(99.0)), math.tan(99)],
            [LazyTensor(torch.tensor(-4.0)), math.tan(-4)],
        ],
    )


def test_scalar_tan_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.tan(a).item(), c),
        [
            [LazyTensor(torch.tensor(0)), 0],
            [LazyTensor(torch.tensor(math.pi)), 0],
            [LazyTensor(torch.tensor(99.0)), math.tan(99)],
            [LazyTensor(torch.tensor(-4.0)), math.tan(-4)],
        ],
    )


def test_scalar_asin_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.asin().item(), c),
        [
            [LazyTensor(torch.tensor(n)), math.asin(n)]
            for n in np.linspace(-1, 1).tolist()
        ],
    )


def test_scalar_asin_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.asin(a).item(), c),
        [
            [LazyTensor(torch.tensor(n)), math.asin(n)]
            for n in np.linspace(-1, 1).tolist()
        ],
    )


def test_scalar_acos_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.acos().item(), c),
        [
            [LazyTensor(torch.tensor(n)), math.acos(n)]
            for n in np.linspace(-1, 1).tolist()
        ],
    )


def test_scalar_acos_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.acos(a).item(), c),
        [
            [LazyTensor(torch.tensor(n)), math.acos(n)]
            for n in np.linspace(-1, 1).tolist()
        ],
    )


def test_scalar_atan_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.atan().item(), c),
        [
            [LazyTensor(torch.tensor(99.0)), math.atan(99)],
            [LazyTensor(torch.tensor(-4.0)), math.atan(-4)],
            [LazyTensor(torch.tensor(-6.0)), math.atan(-6)],
            [LazyTensor(torch.tensor(242.0)), math.atan(242)],
        ],
    )


def test_scalar_atan_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.atan(a).item(), c),
        [
            [LazyTensor(torch.tensor(99.0)), math.atan(99)],
            [LazyTensor(torch.tensor(-4.0)), math.atan(-4)],
            [LazyTensor(torch.tensor(-6.0)), math.atan(-6)],
            [LazyTensor(torch.tensor(242.0)), math.atan(242)],
        ],
    )


def test_scalar_sinh_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.sinh().item(), c),
        [
            [LazyTensor(torch.tensor(n)), math.sinh(n)]
            for n in np.linspace(-1, 1).tolist()
        ],
    )


def test_scalar_sinh_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.sinh(a).item(), c),
        [
            [LazyTensor(torch.tensor(n)), math.sinh(n)]
            for n in np.linspace(-1, 1).tolist()
        ],
    )


def test_scalar_cosh_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.cosh().item(), c),
        [
            [LazyTensor(torch.tensor(n)), math.cosh(n)]
            for n in np.linspace(-1, 1).tolist()
        ],
    )


def test_scalar_cosh_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.cosh(a).item(), c),
        [
            [LazyTensor(torch.tensor(n)), math.cosh(n)]
            for n in np.linspace(-1, 1).tolist()
        ],
    )


def test_scalar_tanh_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.tanh().item(), c),
        [[LazyTensor(torch.tensor(n)), math.tanh(n)] for n in np.linspace(-10, 10)],
    )


def test_scalar_tanh_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.tanh(a).item(), c),
        [[LazyTensor(torch.tensor(n)), math.tanh(n)] for n in np.linspace(-10, 10)],
    )


def test_scalar_asinh_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.asinh().item(), c),
        [
            [LazyTensor(torch.tensor(199.0)), math.asinh(199)],
            [LazyTensor(torch.tensor(-241.0)), math.asinh(-241)],
            [LazyTensor(torch.tensor(-9.0)), math.asinh(-9)],
            [LazyTensor(torch.tensor(0.0)), math.asinh(0)],
        ],
    )


def test_scalar_asinh_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.asinh(a).item(), c),
        [
            [LazyTensor(torch.tensor(199.0)), math.asinh(199)],
            [LazyTensor(torch.tensor(-241.0)), math.asinh(-241)],
            [LazyTensor(torch.tensor(-9.0)), math.asinh(-9)],
            [LazyTensor(torch.tensor(0.0)), math.asinh(0)],
        ],
    )


def test_scalar_acosh_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.acosh().item(), c),
        [
            [LazyTensor(torch.tensor(14.0)), math.acosh(14)],
            [LazyTensor(torch.tensor(2.0)), math.acosh(2)],
            [LazyTensor(torch.tensor(1.0)), math.acosh(1)],
            [LazyTensor(torch.tensor(65.0)), math.acosh(65)],
        ],
    )


def test_scalar_acosh_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.acosh(a).item(), c),
        [
            [LazyTensor(torch.tensor(14.0)), math.acosh(14)],
            [LazyTensor(torch.tensor(2.0)), math.acosh(2)],
            [LazyTensor(torch.tensor(1.0)), math.acosh(1)],
            [LazyTensor(torch.tensor(65.0)), math.acosh(65)],
        ],
    )


def test_scalar_atanh_method() -> None:
    common.call(
        lambda a, c: scalar_isclose(a.atanh().item(), c),
        [
            [LazyTensor(torch.tensor(n)), math.atanh(n)]
            for n in np.linspace(-0.99, 0.99, endpoint=False).tolist()
        ],
    )


def test_scalar_atanh_function() -> None:
    common.call(
        lambda a, c: scalar_isclose(torch.atanh(a).item(), c),
        [
            [LazyTensor(torch.tensor(n)), math.atanh(n)]
            for n in np.linspace(-0.99, 0.99, endpoint=False).tolist()
        ],
    )


def test_run_method() -> None:
    random = torch.randn(3, 4, 5, 6)
    common.call(
        lambda a, b: tensor_allclose(a.run(), b), [[LazyTensor(random), random]]
    )


def test_torch_method() -> None:
    random = torch.randn(3, 4, 5, 6)
    common.call(
        lambda a, b: tensor_allclose(a.torch(), b), [[LazyTensor(random), random]]
    )


def test_numpy_method() -> None:
    random = torch.randn(3, 4, 5, 6)
    common.call(
        lambda a, b: array_allclose(a.numpy(), b.numpy()),
        [[LazyTensor(random), random]],
    )
