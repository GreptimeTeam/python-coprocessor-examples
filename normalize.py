import math

def normalize0(x):
    if x is None or math.isnan(x):
        return 10
    elif x > 10:
        return 100
    elif x < 5:
        return 5
    else:
        return x

@coprocessor(args=["number"], sql="select number from numbers limit 20", returns=["value"])
def normalize(v):
    return [normalize0(x) for x in v]
