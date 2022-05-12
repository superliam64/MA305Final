# integration.py
# routines for numeric integration
# modified from 2022-Apr-21 Jim Hefferon Public Domain

def left_end(x_i,x_iplus1):
    return x_i

def right_end(x_i,x_iplus1):
    return x_iplus1

def midpoint(x_i,x_iplus1):
    return (x_i+x_iplus1)/2

def integral(f, a, b, num_ints, choose_xi=left_end):
    """Compute Reimann sum.
    f  map from reals to reals  Function to be integrated
    a, b  real numbers  Left and right end of integral interval
    num_ints  positive integer  Number of subintervals
    choose_xi  function inputting two reals, outputting a real.  Pick the
        number between the left and right end of each subinterval used
        so that f(xi) is the height of the Reimann box.
    """
    h = (b-a)/num_ints
    total = 0
    if(choose_xi == 'trapezoid'):
        for i in range(num_ints-1):
            subinterval_start = a+i*h
            subinterval_end = subinterval_start+h
            total = total + (f(subinterval_start)+f(subinterval_end)) * h/2
    elif(choose_xi == 'simpsons'):
        for i in range(num_ints-2):
            subinterval = a+(i+1)*h
            if(i%2==0):
                total = total + 2 * f(subinterval)
            else:
                total = total + 4 * f(subinterval)
            
        total = (total + f(a) + f(b))*h
    else :
        for i in range(num_ints):
            subinterval_start = a+i*h
            subinterval_end = subinterval_start+h
            xi = choose_xi(subinterval_start, subinterval_end)
            total = total + f(xi) * h
    return n(total)

INTEGRAL_TABLE_TOLERANCE = n(10^(-10))
def generate_integral_table(f, a, b, choose_xi=midpoint, int_size=6, correct=None):
    for power in range(int_size):
        num_ints = 10**power
        estimate = integral(f, a, b, num_ints, choose_xi)
        output = "number_intervals = ",num_ints," integral estimate =", estimate
        print(output)
        if(correct):
            print("  error=", n(estimate-correct))
            if(estimate and (abs(estimate - correct)) < INTEGRAL_TABLE_TOLERANCE):
                print("  Estimate and correct value are within ", INTEGRAL_TABLE_TOLERANCE)
                break
