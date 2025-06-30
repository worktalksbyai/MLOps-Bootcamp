from logger import logging

def add(a, b):
    logging.info(f"Adding {a} and {b}")
    return a + b

logging.info("Addition function is called")
add(10,15)