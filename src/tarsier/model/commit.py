
from tarsier.model.base import BaseModel


class Commit(BaseModel):
    """Class of commit"""

    def __hash__(self):
        return hash(self.sha)

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
