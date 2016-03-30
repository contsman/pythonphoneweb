#coding=utf-8
import urllib2, sgmllib

urlprefix='http://www.guolvzongbu.com/'

'''
start_tagname(self, attrs)
end_tagname(self)
handle_data(self, text)
tagname就是标签名称，比如当遇到<pre>，就会调用start_pre，遇到</pre>，就会调用 end_pre，attrs即为标签的参数，
以[(attribute, value), (attribute, value), ...]的形式传回，我们要做的就是在其子类重载自己感兴趣标签对应的函数。
'''
# htmlparser
class LinksParser(sgmllib.SGMLParser):
    urls = []
    def start_a(self, attrs):
        for name, value in attrs:
            if name == 'href' and value not in self.urls:
                if value.endswith('html') and not self.urls.__contains__(urlprefix[0:-1]+value) and not '/contact/index.html'.__eq__(value) and not '/about/index.html'.__eq__(value):
                    self.urls.append(urlprefix[0:-1]+value)
                else:
                    continue
                # return
    def end_a(self):
        print 'end_a tag.'

    # def handle_data(self, data):
    #     print data

p = LinksParser()
paths = ['/', '1/', '2/', 'duoriyou/', 'zhoubianyou/']
for path in paths:
    url = urlprefix+path
    f = urllib2.urlopen(url)
    html = f.read().decode("gbk").encode("utf-8") #characterset
    p.feed(html)

## calculate number of urls
i = 0
## write url data to local file on disk.
file_object = open('d:/thefile.txt', 'w')

## append data for http url post.
data=''
for url in p.urls:
    i=i+1
    data=data+url+'\n'
    print url
    file_object.write(url)
# file_object.writelines(p.urls)
file_object.close( )
print 'Has url count:',i
f.close()
p.close()

## start execute submit url to baiduzhanzhang.
# if __name__ == 'main':
#     url = '/urls?site=www.guolvzongbu.com&token=V9h3CvBDsnmwv4oc'
#     headerdata={'User-Agent':'curl/7.12.1','Host':'data.zz.baidu.com'}
#     conn = httplib.HTTPConnection("data.zz.baidu.com")
#     conn.request(method="POST",url=url,body=data,headers= headerdata)
#     response = conn.getresponse()
#     res= response.read()
#     print res
#     response.close()
#     conn.close()