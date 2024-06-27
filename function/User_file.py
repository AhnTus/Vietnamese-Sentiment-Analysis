class User:
    def __init__(self,username=None,password=None,comment=None,userid=None,predict=None):
        self._userid=userid
        self._username=username
        self._password=password
        self._comment=comment 
        self._predict=predict
    @property
    def getPredict(self):
        return self._predict
    @property
    def getUserName(self):
        return self._username
    @property
    def getPassWord(self):
        return self._password
    @property
    def getComment(self):
        return self._comment
    @property
    def getUserId(self):
        return self._userid