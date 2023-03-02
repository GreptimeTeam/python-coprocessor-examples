from greptime import vector

@copr(returns=["value"])
def list_comprehension() -> (vector[f64]):
    a = vector([1.0, 2.0, 3.0])
    # This returns a vector([3.0, 4.0])
    return [x+1 for x in a if x >= 2.0]
