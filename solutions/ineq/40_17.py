"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 5
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 5 = 17.65
Came to:
2.00x >  17.65
Result:
x < 8.825
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 5")
# -------------------------------------------------
