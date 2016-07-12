

class Book(BaseModel):

    def __init__(self, name=None, isbn=None):
        self.name = name
        self.isbn = isbn

    def __repr__(self):
        return '<Book name=%s ISBN=%s />' % (self.name, self.isbn)

    @property
    def full_name(self):
        return '%s %s' % (self.isbn, self.name)