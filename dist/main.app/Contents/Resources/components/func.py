def tup_sub(tu1, tu2):
    # result = tuple()
    result = (tu1[0] - tu2[0], tu1[1] - tu2[1])
    return result

def tup_add(tu1, tu2):
    # result = tuple()
    result = (tu1[0] + tu2[0], tu1[1] + tu2[1])
    return result

def tup_mul(tu1, ft):
    # result = tuple()
    result = (tu1[0]* ft, tu1[1] * ft)
    return result

# function below calculate the relevant velocity when the ball the wall
# multiply x pos with st
def tup_mul_x(tup1, st):
    return (tup1[0] * st, tup1[1])

def tup_mul_y(tup1, st):
    return (tup1[0], tup1[1] * st)

def tup_add_x(tup1, st):
    return (tup1[0] + st, tup1[1])

def tup_add_y(tup1, st):
    return (tup1[0], tup1[1] + st)