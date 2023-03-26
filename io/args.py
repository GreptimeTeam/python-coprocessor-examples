@coprocessor(args=["a", "b"],
             returns=["value"],
             sql="select number as a,number as b from numbers limit 10")
def add_vectors(a, b) -> vector[i64]:
    return a + b
