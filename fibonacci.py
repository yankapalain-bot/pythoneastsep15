def calculate_fibonacci(n):
    """
    Calculates the nth number in the Fibonacci sequence.
    Example:
    calculate_fibonacci(0) -> 0
    calculate_fibonacci(1) -> 1
    calculate_fibonacci(5) -> 5
    """
  
    # TODO: Student must write their code here.
    if n == 0: 
        return 0
    elif n < 0: 
        raise ValueError("The number must be positive integer ")
        
    
    x, y = 0, 1
    for _ in range(2, n + 1):
        x, y = y, x + y

    return y



 

