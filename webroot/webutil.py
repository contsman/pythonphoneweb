class WebUtil:
    def isAndriod(self,request):
        ua = request.headers['User-Agent']
        return ua.__contains__('Android')
    def isIphone(self,request):
        ua = request.headers['User-Agent']
        return ua.__contains__('iPhone')

    def isSmartPhone(self,request):
        ua = request.headers['User-Agent']
        return ua.__contains__('iPhone') or ua.__contains__('Android')
    def redirectPath(self,request):
        if self.isAndriod(request):
            return 'android/'
        elif self.isIphone(request):
            return 'iphone/'
        else:
            return 'pc/'