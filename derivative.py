def derive(f,a,h):
    return (f(a+h)-f(a-h))/(2*h)

def generate_derivative_table(f,a,span,correct=None):
    for power in range(span):
        h = 10**(-1*power)
        estimate = n(derive(f, a, h))
        output = "h = ",h," difference quotient =", estimate
        print(output)
        if(correct):
            print("  error=", n(estimate-correct))
        