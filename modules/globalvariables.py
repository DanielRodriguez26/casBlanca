import mysql.connector


class GlobalVariables(object):
    def __init__(self, i_var=None):
        self.__i_var = i_var
        self.MysqlHost="localhost"
        self.MysqlUser="dibankaops"
        self.MysqlPassword="37f75cac-bcbd-11ea-a5ee-00090ffe0001"
        self.MysqlDatabase="casaBlanca"

        self.__msql= mysql.connector.connect(
                        host=self.MysqlHost,
                        user=self.MysqlUser,
                        password=self.MysqlPassword,
                        database=self.MysqlDatabase)  