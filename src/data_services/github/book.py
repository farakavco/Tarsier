

class BookStaticDataService(BaseDataService):
    _static_data = [
        {
            'name': 'Something',
            'isbn': 'w3423423423gh423h42'
        },
        {
            'name': 'Alchemist',
            'isbn': 'w34234223gh423h42'
        }

    ]

    def get_all(self):
        for d in self._static_data:
            yield Book(**d)
