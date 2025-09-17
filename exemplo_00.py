from loguru import logger
from sys import stderr 


logger.add("meu_app.log", level="CRITICAL")

logger.add(
                "meu_arquivo_de_logs_critical.log",
                format="{time} {level} {message} {file}",
                level="ERROR"
            )

logger.add(
                "meu_arquivo_de_logs_critical.log",
                format="{time} {level} {message} {file}",
                level="INFO"
            )

logger.add(
                "meu_arquivo_de_logs_critical.log",
                format="{time} {level} {message} {file}",
                level="CRITICAL"
            )

def soma(x,y):
    logger.info(x)
    logger.info(y)
    logger.info(x + y)
    return x + y

print(soma(2,3))