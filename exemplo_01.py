from utils_log import log_decorator

#pydantic
#pandera

@log_decorator
def soma(x,y):
    return x + y

print(soma(2,3))