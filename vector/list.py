from greptime import vector

@copr(returns=["value"])
def answer() -> (vector[i64]):
    return vector([42, 43, 44])
