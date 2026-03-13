🚀 Funcionalidades
1. Resultado Aritmético de Bloco
Operadores: sum, mult, avg, diff, const, integ
Descrição: Calcula operações matemáticas diretamente em blocos de números.
2. Estatística Avançada
Operadores: median, std, var, min, max, range
Descrição: Aplicações estatísticas avançadas em blocos de dados.
3. Trigonometria
Operadores: sin, cos, tan, wave
Descrição: Operações trigonométricas aplicadas a listas de números.
4. Transformações Matemáticas
Operadores: sqrt, log, pow, abs, ceil, floor
Descrição: Transformações matemáticas comuns aplicadas a blocos de dados.
5. Data Cleaning
Operadores: norm, clip, limit, approx
Descrição: Limpeza e normalização de blocos de dados.
6. Regra SBU
Lógica de Ajuste (Adjustment): Aplica ajustes derivados automaticamente; se o bloco mudar, todas as funções derivadas recalculam seus resultados.

⚡ Exemplo de Uso

Python
Copiar código
from oriebir_math import SBU

# 1. Inicializa o motor SBU
sbu = SBU()

# 2. Define o bloco de entrada
data = [10.5, 20.2, 30.8, 5.1]

# 3. Executa a operação "sum" com ajustes
result = sbu.eject(input_block=data, op="sum", adjustment=[1.5, 2.5])

print(f"Resultado Final: {result}")
# Cálculo interno: (10.5 + 20.2 + 30.8 + 5.1) - (1.5 + 2.5) = 62.6


✅ A lógica derivativa garante que se você alterar data ou adjustment, todas as funções dependentes se ajustam automaticamente.
🧪 Testes
Execute os testes com:
Bash
Copiar código
pip install pytest
pytest tests/test_sbu_complete.py
Todos os operadores e regras da SBU estão validados e funcionando.
📦 Instalação
Bash
Copiar código
pip install oriebir-math