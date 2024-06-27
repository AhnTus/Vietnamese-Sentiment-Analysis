class Comment:
    def __init__(self,comment_id=None,comment=None,predict=None):
        self._comment=comment 
        self._predict=predict
        self._comment_id=comment_id
    @property
    def getPredict(self):
        return self._predict
    @property
    def getComment(self):
        return self._comment
    @property
    def getId(self):
        return self._comment_id