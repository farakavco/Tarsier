
from tarsier.model.base import BaseModel


class Commit(BaseModel):
    """Class of commit"""

    def __hash__(self):
        return 0

    def __eq__(self, other):
        return self.sha == other.sha
