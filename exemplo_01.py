from loguru import logger
from sys import stderr 


def soma(x,y):
    logger.info(x)
    logger.info(y)
    logger.info(x + y)
    return x + y

print(soma(2,3))