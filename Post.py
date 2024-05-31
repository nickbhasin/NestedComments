class Post:

    def __init__(self, id, title, user_id, created_at) -> None:

        self.id = id
        self.title = title
        self.user_id = user_id
        self.created_at = created_at

    def getId(self):
        return self.id

    def setId(self, value):
        self.id = value