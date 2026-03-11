from .operators import *

class SBU:
    def __init__(self):
        self.operators = {
            "sum": sum_op, "mult": mult_op, "avg": avg_op,
            "sqrt": sqrt_op, "diff": diff_op, "approx": approx_op,
            "wave": wave_op, "limit": limit_op, "const": const_op,
            "integ": integ_op,
            # Novos registros V1.0.2
            "median": median_op, "std": stdev_op, "var": var_op,
            "min": min_op, "max": max_op, "range": range_op,
            "sin": sin_op, "cos": cos_op, "tan": tan_op,
            "log": log_op, "exp": exp_op, "pow": pow_op,
            "ceil": ceil_op, "floor": floor_op, "abs": abs_op,
            "norm": norm_op, "clip": clip_op,
        }

    def eject(self, input_block, op, adjustment=None, **kwargs):
        if op not in self.operators:
            raise ValueError(f"Operator '{op}' not recognized.")

        result = self.operators[op](input_block, **kwargs)

        if adjustment:
            adj_sum = sum(adjustment)
            if isinstance(result, (int, float)):
                return result - adj_sum
            elif isinstance(result, list):
                return [n - adj_sum for n in result]

        return result