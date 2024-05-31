class Comment:
    def __init__(self, title, id, post_id, user_id, parent_comment_id=None, is_parent=False):
        self.post_id = post_id
        self.user_id = user_id
        self.title = title
        self.id = id
        self.parent_comment_id = parent_comment_id
        self.isParent = is_parent

    def getTitle(self):
        return self.title

    def setTitle(self, value):
        self.title = value

    def getParentId(self):
        return self.parent_comment_id

    def setParentId(self, value):
        self.parent_comment_id = value

    def getId(self):
        return self.id

    def getPostId(self):
        return self.post_id

    def setPostId(self, value):
        self.post_id = value

    def getUserID(self):
        return self.user_id

    def setUserID(self, value):
        self.user_id = value


