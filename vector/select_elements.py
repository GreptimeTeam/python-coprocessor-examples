from greptime import vector

@copr(returns=["value"])
def select_elements() -> (vector[f64]):
    a = vector([1.0, 2.0, 3.0])
    # This returns a vector([2.0, 3.0])
    return a[a>=2.0]
