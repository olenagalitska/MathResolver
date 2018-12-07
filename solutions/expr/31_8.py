"""
  ( 3 )  / ( sin ( 45 ) )  * 18
-------------------------------------------------

Compute individual results:
sin(45.0) => 0.85
3.0 / 0.85 => 3.53
3.53 * 18.0 => 63.54
Result: 63.54
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve("  ( 3 )  / ( sin ( 45 ) )  * 18")
# -------------------------------------------------
