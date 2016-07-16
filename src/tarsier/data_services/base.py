

class BaseDataService(object):
    """Base model of data services"""

    @classmethod
    def get_commits(cls, **kwargs):
        raise NotImplementedError
