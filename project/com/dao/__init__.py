import pymysql

def con_db():
    return pymysql.connect(host='localhost',
                            user='root',
                            password='root',
                            db='stock_market',
                            cursorclass=pymysql.cursors.DictCursor
                            )