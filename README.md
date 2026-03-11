🛠️ Symbol Table (Available Operators)
Use these symbols in the op parameter of the eject method to perform instantaneous calculations:

🛠️ SBU Operator Table (Version 1.0.2)
Symbol (op),Internal Function,Operation Description
"""sum""",sum_op,Total sum of all block elements.
"""mult""",mult_op,Product (multiplication) of all items.
"""avg""",avg_op,Calculates the simple arithmetic mean.
"""sqrt""",sqrt_op,Calculates the square root of each individual element.
"""diff""",diff_op,Difference between the last and the first term of the block.
"""approx""",approx_op,Rounding of values (default: 2 decimal places).
"""wave""",wave_op,Applies oscillatory function (sin(n) * cos(n)).
"""limit""",limit_op,Noise filter (zeros values below a tolerance).
"""const""",const_op,Multiplication of all elements by a constant c.
"""integ""",integ_op,Simple numerical integration (Total Sum * Step).
"""median""",median_op,Calculation of the central value (median) of the data block.
"""std""",std_op,Measure of statistical dispersion (standard deviation).
"""min""",min_op,Returns the smallest value found in the block.
"""max""",max_op,Returns the largest value found in the block.
"""range""",range_op,Difference between the maximum and minimum value (amplitude).
"""sin""",sin_op,Applies the Sine function to each individual element.
"""cos""",cos_op,Applies the Cosine function to each individual element.
"""tan""",tan_op,Applies the Tangent function to each individual element.
"""log""",log_op,Natural logarithm (base e) of the elements.
"""pow""",pow_op,Raises elements to a power p (default 2).
"""norm""",norm_op,Rescales the block to the linear scale [0, 1].
"""clip""",clip_op,Keeps values within a defined interval (min/max).
"""abs""",abs_op,Absolute value (positive) of each element in the block.
"""ceil""",ceil_op,Rounds each element to the upper integer.
"""floor""",floor_op,Rounds each element to the lower integer.
"""var""",var_op,Calculation of the statistical variance of the data block.

📖 Usage Example (Visual Sample)
See how the SBU engine processes a list of data with fine adjustment:

Python
from oriebir_math import SBU

# 1. Initialize the SBU engine
sbu = SBU()

# 2. Define your input block
data = [10.5, 20.2, 30.8, 5.1]

# 3. Execute the operation with an Adjustment
# The SBU rule subtracts the sum of 'adjustment' from the result of the 'op' operation.
result = sbu.eject(
    input_block=data, 
    op="sum", 
    adjustment=[1.5, 2.5]
)

pip install pytest

pytest tests/test_sbu_complete.py


print(f"Final Result: {result}") 
# Internal calculation: (10.5 + 20.2 + 30.8 + 5.1) - (1.5 + 2.5) = 62.6

======================= TEST SESSION SUMMARY =======================
Plataforma: win32 | Python: 3.13.11 | Pytest: 9.0.2
Diretório Raiz: oriebir_math_project
Configuração: pyproject.toml

Coletados: 27 itens
Status: 27 PASSED (100% de aproveitamento)
Tempo de execução: 0.16s
====================================================================

Categoria,Operadores Validados,Resultado
Aritmética de Bloco,"sum, mult, avg, diff, const, integ",PASS ✅
Estatística Avançada,"median, std, var, min, max, range",PASS ✅
Trigonometria,"sin, cos, tan, wave",PASS ✅
Transformações,"sqrt, log, pow, abs, ceil, floor",PASS ✅
Data Cleaning,"norm, clip, limit, approx",PASS ✅
Regra SBU,Lógica de Ajuste (Adjustment),PASS ✅
