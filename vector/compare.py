from greptime import vector

@copr(returns=["value"])
def compare() -> vector[bool]:
    # This returns a vector([False, False, True])
    return vector([1.0, 2.0, 3.0]) > 2.0
