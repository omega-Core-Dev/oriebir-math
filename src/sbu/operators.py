import math
import statistics
from functools import reduce
from operator import mul

# --- Operadores Básicos (Originais) ---
def sum_op(x): return sum(x)
def mult_op(x): return math.prod(x) if hasattr(math, 'prod') else reduce(mul, x, 1)
def avg_op(x): return sum(x)/len(x) if x else 0
def sqrt_op(x): return [math.sqrt(n) for n in x]
def diff_op(x): return x[-1] - x[0] if len(x) >= 2 else 0
def approx_op(x, decimals=2): return [round(n, decimals) for n in x]
def wave_op(x): return [math.sin(n) * math.cos(n) for n in x]
def limit_op(x, tol=0.001): return [n if n > tol else 0 for n in x]
def const_op(x, c=1): return [n * c for n in x]
def integ_op(x, step=0.1): return sum(x) * step

# --- Novos Operadores V1.0.2 ---

# Estatística
def median_op(x): return statistics.median(x) if x else 0
def stdev_op(x): return statistics.stdev(x) if len(x) > 1 else 0
def var_op(x): return statistics.variance(x) if len(x) > 1 else 0

# Extremos e Ranges
def min_op(x): return min(x) if x else 0
def max_op(x): return max(x) if x else 0
def range_op(x): return max(x) - min(x) if x else 0

# Trigonometria Pura
def sin_op(x): return [math.sin(n) for n in x]
def cos_op(x): return [math.cos(n) for n in x]
def tan_op(x): return [math.tan(n) for n in x]

# Logaritmos e Exponenciais
def log_op(x): return [math.log(n) if n > 0 else 0 for n in x]
def exp_op(x): return [math.exp(n) for n in x]
def pow_op(x, p=2): return [math.pow(n, p) for n in x]

# Arredondamento e Inteiros
def ceil_op(x): return [math.ceil(n) for n in x]
def floor_op(x): return [math.floor(n) for n in x]
def abs_op(x): return [abs(n) for n in x]

# Processamento de Dados
def norm_op(x): 
    """Normaliza o bloco entre 0 e 1."""
    if not x or max(x) == min(x): return [0] * len(x)
    ma, mi = max(x), min(x)
    return [(n - mi) / (ma - mi) for n in x]

def clip_op(x, min_val=0, max_val=1):
    """Limita os valores entre um mínimo e um máximo."""
    return [max(min_val, min(n, max_val)) for n in x]