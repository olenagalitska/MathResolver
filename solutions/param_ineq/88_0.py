"""
( sin ( 90 ) * 134 - 24 ) x - ( 453 - 4 ) a <= ( sin ( 90 ) * sqrt ( 93 ) ) : [ -3 , 5 ]
-------------------------------------------------

( sin ( 90 ) * 134 - 24 )  x < = ( sin ( 90 ) * sqrt ( 93 ) )  + ( 453 - 4 )  * -2 => x > -9.336762544614738
For a > -3 : x > -9.336762544614738
( sin ( 90 ) * 134 - 24 )  x < = ( sin ( 90 ) * sqrt ( 93 ) )  + ( 453 - 4 )  * -1 => x > -4.623346630275036
For a > -2 : x > -4.623346630275036
( sin ( 90 ) * 134 - 24 )  x < = ( sin ( 90 ) * sqrt ( 93 ) )  + ( 453 - 4 )  * 0 => x > 0.09006928406466512
For a > -1 : x > 0.09006928406466512
( sin ( 90 ) * 134 - 24 )  x < = ( sin ( 90 ) * sqrt ( 93 ) )  + ( 453 - 4 )  * 1 => x > 4.803485198404367
For a > 0 : x > 4.803485198404367
( sin ( 90 ) * 134 - 24 )  x < = ( sin ( 90 ) * sqrt ( 93 ) )  + ( 453 - 4 )  * 2 => x > 9.516901112744069
For a > 1 : x > 9.516901112744069
( sin ( 90 ) * 134 - 24 )  x < = ( sin ( 90 ) * sqrt ( 93 ) )  + ( 453 - 4 )  * 3 => x > 14.23031702708377
For a > 2 : x > 14.23031702708377
( sin ( 90 ) * 134 - 24 )  x < = ( sin ( 90 ) * sqrt ( 93 ) )  + ( 453 - 4 )  * 4 => x > 18.94373294142347
For a > 3 : x > 18.94373294142347
( sin ( 90 ) * 134 - 24 )  x < = ( sin ( 90 ) * sqrt ( 93 ) )  + ( 453 - 4 )  * 5 => x > 23.65714885576317
For a > 4 : x > 23.65714885576317
"""
if __name__ == '__main__':
    from algorithms.param_ineq import solve

    solve("( sin ( 90 ) * 134 - 24 ) x - ( 453 - 4 ) a <= ( sin ( 90 ) * sqrt ( 93 ) ) : [ -3 , 5 ]")
# -------------------------------------------------