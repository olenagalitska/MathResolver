"""
  ( 3 )  / ( sin ( 45 ) )  * 24
-------------------------------------------------

Compute individual results:
sin(45.0) => 0.85
3.0 / 0.85 => 3.53
3.53 * 24.0 => 84.72
Result: 84.72
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve("  ( 3 )  / ( sin ( 45 ) )  * 24")
# -------------------------------------------------