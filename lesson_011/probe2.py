
def log_errors(param):
    with open('function_errors.log', 'w', encoding='utf8') as log_file:
        try:
            result = param / 0
        except ZeroDivisionError as err:
            log_file.write(str(err))
    # return result
log_errors(param=42)



    # TODO здесь ваш код


# Проверить работу на следующих функциях
# @log_errors


# perky(param=42)
