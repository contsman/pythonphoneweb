#coding=utf-8
from flask import Flask, request, render_template
import dbutil
from webroot.webutil import WebUtil
app = Flask(__name__)
wutil = WebUtil()
@app.route('/',methods=['GET','POST'])
def index():
    sql='select id,typename,description from dede_arctype'
    linelist = dbutil.list(sql)
    # for list in linelist:
    #     print("linelist id[%s]" % list[0])
    sections = dbutil.getHomeSection()
    swipes = dbutil.getSwipes()
    path = wutil.redirectPath(request)
    return render_template(path+'index.html',sections = sections,swipes = swipes)

@app.route('/signin', methods=['GET'])
def signin_form():
    path = wutil.redirectPath(request)
    return render_template('login.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    rowcount = dbutil.login(username,password)
    if rowcount>=1:
        page_list=[1,2,3,4,5]
        return render_template('sign-ok.html', username=username,page_list=page_list)
    return render_template('login.html', message='Bad username or password', username=username)

@app.route('/vpl',methods=['GET'])
def vpl():
    path = wutil.redirectPath(request)
    return render_template(path+'list.html')

@app.route('/detail',methods=['GET'])
def detail():
    id = request.args.get('aid')
    path = wutil.redirectPath(request)
    return render_template(path+'list.html')

if __name__ == '__main__':
    app.run(host='192.168.2.7',debug=True)