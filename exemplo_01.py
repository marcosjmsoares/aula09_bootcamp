from utils_log import log_decorator
from timer_decorator import time_measure_decorator
import time
#pydantic
#pandera

@log_decorator
@time_measure_decorator
def soma(x,y):
    time.sleep(5)
    return x + y

print(soma(2,3))