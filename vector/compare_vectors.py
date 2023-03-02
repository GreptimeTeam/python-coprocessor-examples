from greptime import vector

@copr(returns=["value"])
def compare_vectors() -> vector[bool]:
    # This returns a vector([False, False, True])
    return vector([1.0, 2.0, 3.0]) > vector([1.0, 2.0, 2.0])
