import sys
import os
import math
import pytest

# Garante que o Python encontre a pasta 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from sbu import SBU
bib = SBU()

# --- OPERADORES BÁSICOS (10) ---
def test_sum(): assert bib.eject([1, 2, 3], 'sum') == 6
def test_mult(): assert bib.eject([2, 3, 4], 'mult') == 24
def test_avg(): assert bib.eject([2, 4, 6], 'avg') == 4
def test_sqrt(): assert bib.eject([4, 16], 'sqrt') == [2.0, 4.0]
def test_diff(): assert bib.eject([10, 50], 'diff') == 40
def test_approx(): assert bib.eject([3.14159], 'approx') == [3.14]
def test_wave(): assert isinstance(bib.eject([1], 'wave'), list)
def test_limit(): assert bib.eject([0.0001, 0.1], 'limit') == [0, 0.1]
def test_const(): assert bib.eject([1, 2], 'const', c=10) == [10, 20]
def test_integ(): assert math.isclose(bib.eject([1, 1], 'integ', step=0.5), 1.0)

# --- ESTATÍSTICA (6) ---
def test_median(): assert bib.eject([1, 10, 5], 'median') == 5
def test_std(): assert math.isclose(bib.eject([1, 2, 3], 'std'), 1.0)
def test_var(): assert math.isclose(bib.eject([1, 2, 3], 'var'), 1.0)
def test_min(): assert bib.eject([10, 2, 5], 'min') == 2
def test_max(): assert bib.eject([10, 2, 5], 'max') == 10
def test_range(): assert bib.eject([10, 2, 5], 'range') == 8

# --- TRIGONOMETRIA (3) ---
def test_sin(): assert math.isclose(bib.eject([0], 'sin')[0], 0.0)
def test_cos(): assert math.isclose(bib.eject([0], 'cos')[0], 1.0)
def test_tan(): assert math.isclose(bib.eject([0], 'tan')[0], 0.0)

# --- MATEMÁTICA AVANÇADA (2) ---
def test_log(): assert bib.eject([math.e], 'log') == [1.0]
def test_pow(): assert bib.eject([2], 'pow', p=3) == [8.0]

# --- PROCESSAMENTO E DATA (5) ---
def test_norm(): assert bib.eject([0, 5, 10], 'norm') == [0.0, 0.5, 1.0]
def test_clip(): assert bib.eject([-1, 0.5, 2], 'clip') == [0, 0.5, 1]
def test_ceil(): assert bib.eject([1.1], 'ceil') == [2]
def test_floor(): assert bib.eject([1.9], 'floor') == [1]
def test_abs(): assert bib.eject([-5, 10], 'abs') == [5, 10]

# --- LÓGICA DE MOTOR (1) ---
def test_adjustment_logic():
    # sum([10, 10]) = 20. Adjustment [5] = 5. Result: 20 - 5 = 15.
    assert bib.eject([10, 10], 'sum', adjustment=[5]) == 15

if __name__ == "__main__":
    pytest.main(["-v", __file__])