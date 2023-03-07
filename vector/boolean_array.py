from greptime import vector

@copr(returns=["value"])
def boolean_array() -> vector[f64]:
    v = vector([1.0, 2.0, 3.0])
    # This returns a vector([2.0])
    return v[(v > 1) & (v< 3)]
