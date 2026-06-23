import pymysql

def conectar():
    return pymysql.connect(
        host="bq9okaaycr9dgkr9ldre-mysql.services.clever-cloud.com",
        user="u5nzjsbpntl2i1dg",
        password="4ghDBkdgMFDPvesd68WW",
        database="bq9okaaycr9dgkr9ldre",
        port=3306
    )
