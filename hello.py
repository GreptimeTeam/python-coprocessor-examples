@coprocessor(returns=['msg'])
def hello() -> vector[str]:
   return "hello, GreptimeDB"
