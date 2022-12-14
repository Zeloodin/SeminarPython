
sqrt = lambda n,p=2:n ** (1/p)
pow = lambda n,p=2: n ** p

def sign(sgn,first,second=None):
    if second != None:
        match sgn:
            case "+":
                return first+second
            case "-":
                return first-second
            case "*":
                return first*second
            case "/":
                return first/second
            case "^", "**":
                return first ** second
            case "//", "√":
                return first ** (1/second)
            case "%":
                return first % second
            case _:
                pass
    else:
        match sgn:
            case "+":
                return first
            case "++":
                return first + 1
            case "-":
                return -first
            case "--":
                return first - 1
            case "*":
                return first * 2
            case "**","^":
                return first ** 2
            case "/":
                return first / 2
            case "//","√":
                return first ** 0.5
