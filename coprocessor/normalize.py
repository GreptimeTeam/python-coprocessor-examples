import math

def normalize0(x):
    if x is None or math.isnan(x):
        return 0
    elif x > 5:
        return 5
    elif x < 0:
        return 0
    else:
        return x

@coprocessor(args=["number"],
             sql="select number from numbers limit 10", returns=["value"])
def normalize(v) -> vector[i64]:
    return [normalize0(x) for x in v]
