"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 1
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 1 = 3.53
Came to:
2.00x >  3.53
Result:
x < 1.765
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 1")
# -------------------------------------------------
