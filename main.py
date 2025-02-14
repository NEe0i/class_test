from loguru import logger

from parser import Parser


def main():
    
    logger.add('file.log',
               format = '{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}',
               rotation = "3 days",
               backtrace=True,
               diagnose=True)
    
    title = input("Введите название новеллы: ")
    url = input("Вве")