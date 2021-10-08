import logging as lg


class Logg:
    def __init__(self, name):
        """
        Function is used to instantiate the custom logger
        :param name: custom name for the logger
        """
        try:
            # Creating Custom Logger
            self.logger = lg.getLogger(name)

        except Exception as e:
            raise Exception(e)

    def initialize_logger(self):
        try:
            formatter = lg.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                                     datefmt='%Y-%m-%d  %H:%M:%S')

            # Creating Handlers
            file_handler = lg.FileHandler('testlog.log')

            # Adding Formatters to the Handlers
            file_handler.setFormatter(formatter)

            # Adding Handler to loggers
            self.logger.addHandler(file_handler)

            return self.logger
        except Exception as e:
            raise Exception(e)

    def print_log(self, log_statement, log_level):
        """
        This function is use for printing and logging the statements
        :param log_statement: Statement for logging
        :param log_level : Level of log that needs to be maintained
        """
        try:

            if log_level == 'error':
                self.logger.error(log_statement)

            elif log_level == 'exception':
                self.logger.exception(log_statement)

        except Exception as e:
            raise Exception(e)
