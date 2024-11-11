import  logging

logging.basicConfig(level=logging.DEBUG,
                    filename='test.log',
                    filemode='w',
                    encoding='utf-8',
                    format='We have next log message: %(levelname)s: %(asctime)s - %(message)s'
                    )


# logging.debug("Debug message")
# logging.info("Info message")
# logging.warning("Warning message !!!")
# logging.error("Error message !!!")
# logging.critical("Critical message !!!")

try:
    print(10/0)
except ZeroDivisionError as error:
    print(error)
    logging.exception(error.args)