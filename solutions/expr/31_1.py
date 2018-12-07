"""
  ( 3 )  / ( sin ( 45 ) )  * 11
-------------------------------------------------

Compute individual results:
sin(45.0) => 0.85
3.0 / 0.85 => 3.53
3.53 * 11.0 => 38.83
Result: 38.83
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve("  ( 3 )  / ( sin ( 45 ) )  * 11")
# -------------------------------------------------
