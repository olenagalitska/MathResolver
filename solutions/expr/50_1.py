"""
 ( sin ( 90 ) * sqrt ( 93 ) )  + ( 453 - 4 )  * -1
-------------------------------------------------

1. Compute individual results:
sin(90.0) => 0.89
sqrt(93.0) => 9.64
0.89 * 9.64 => 8.58
453.0 - 4.0 => 449.0
449.0 * -1.0 => -449.0
8.58 + -449.0 => -440.42
2. Result: -440.42
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve(" ( sin ( 90 ) * sqrt ( 93 ) )  + ( 453 - 4 )  * -1")
# -------------------------------------------------