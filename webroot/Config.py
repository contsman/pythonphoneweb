import ConfigParser


class Config:
        def __init__(self, config_file_path):
                cf = ConfigParser.ConfigParser()
                cf.read(config_file_path)

                s = cf.sections()
                print 'section:', s

                o = cf.options("baseconf")
                print 'options:', o

                v = cf.items("baseconf")
                print 'db:', v

                db_host = cf.get("baseconf", "db_host")
                db_port = cf.getint("baseconf", "db_port")
                db_user = cf.get("baseconf", "db_user")
                db_pwd = cf.get("baseconf", "db_pwd")
                db_db = cf.get("baseconf", "db_db")
                self.db_host = db_host
                self.db_port = db_port
                self.db_user = db_user
                self.db_pwd = db_pwd
                self.db_db = db_db
