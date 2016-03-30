#coding=utf-8
import mysql.connector,random
from webroot.Config import Config
#     cf.set("baseconf", "db_pass", "123456")
#     cf.write(open(config_file_path, "w"))
# if __name__ == "__main__":
#   f = Db_Connector("../conf/db_config.ini")
conf = Config("config/config.ini")
def getConn():
    conn = mysql.connector.connect(user=conf.db_user, password=conf.db_pwd, database=conf.db_db, use_unicode=True)
    return conn

def insert(sql):
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    rowcount = cursor.rowcount
    cursor.close()
    conn.close
    return rowcount

def delete(sql):
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    rowcount = cursor.rowcount
    cursor.close()
    conn.close
    return rowcount

def login(username,password):
    rowcount = 0
    try:
        sql = 'select * from users where username = "%s" and password = "%s"' % (username,password)
        conn = getConn()
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchone()
        if isinstance(rows,tuple):
            rowcount = rows[0]
        cursor.close()
        conn.close
    except Exception as e:
        print("Login Exception:%s" % e.message)
    return rowcount

def list(sql):
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    conn.close
    return rows

def getHomeSection():
    sql='select id,typename,description from dede_arctype'
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()

    sections = []
    for row in rows:
        section = {}
        #a.aid,a.typeid,a.xlts,a.xlxc,a.fysm,a.zyts,a.mddxx,a.crjg,a.etjg,a.tjly,a.bjrq,a.cfdd,a.fkfs,a.ftrq,a.tyzl,a.yhzc,a.dxnr,a.msjg,b.id,b.title,b.shorttitle,b.click,b.litpic,b.keywords
        sql1 = 'select a.aid,a.typeid,a.crjg,a.msjg,b.title,b.shorttitle,b.litpic,b.click from dede_line a,dede_archives b where a.aid = b.id and a.typeid = "%s"' % (row[0])
        cursor.execute(sql1)
        lines = cursor.fetchall()
        if lines.__len__()>1:
            section['type'] = row
            section['lines'] = random.sample(lines, 2)
            sections.append(section)
    return sections


def getSwipes():
    sql='select a.aid,a.typeid,a.crjg,a.msjg,b.title,b.shorttitle,b.litpic,b.click from dede_line a,dede_archives b where a.aid = b.id'
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute(sql)
    lines = cursor.fetchall()
    for line in lines:
        print(line)
    return random.sample(lines,5)