@copr(args=["n1", "n2"],
      returns=["value"],
      sql="select number as n1,number as n2 from numbers limit 5")
def add_vectors(n1, n2) -> vector[i32]:
    return n1 + n2
