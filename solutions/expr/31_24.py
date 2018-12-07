"""
  ( 3 )  / ( sin ( 45 ) )  * 34
-------------------------------------------------

Compute individual results:
sin(45.0) => 0.85
3.0 / 0.85 => 3.53
3.53 * 34.0 => 120.02
Result: 120.02
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve("  ( 3 )  / ( sin ( 45 ) )  * 34")
# -------------------------------------------------
