@coprocessor(args=["number", "number"], returns=["value"])
def add_vectors(a, b) -> vector[i64]:
    return a + b
