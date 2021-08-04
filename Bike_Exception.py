class EmptyFuelException(Exception):
    def __init__(self):
        super(EmptyFuelException, self).__init__()


class NoOnException(Exception):
    def __init__(self):
        super(NoOnException, self).__init__()
