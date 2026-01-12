"""Scenario 2: Logging DecoratorTask: Create a decorator @log_execution_time that logs the time taken 
to execute a function. Use it to log the runtime of a sample function calculate_sum(n) that returns the 
sum of numbers from 1 to n."""


from datetime import datetime


def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        duration = end - start
        print("Execution time:", duration.total_seconds(), "seconds")
        return result
    return wrapper


@log_execution_time
def calculate_sum(n):
    return sum(range(1, n + 1))


output = calculate_sum(1000000)
print("Sum is:", output)
