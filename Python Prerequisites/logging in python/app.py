import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("/Users/aple/Documents/VSCode_GitHub/MLOps Bootcamp/Python Prerequisites/logging in python/app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Arithematic App")


def add(a,b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

add(5,10)