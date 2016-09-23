from src.abc_base import BASE_Localizer

class Simple_Localizer(BASE_Localizer):

    def __init__(self):
        super(Simple_Localizer, self).__init__()

    def load_pattern(self):
        raise NotImplementedError()

    def training(self):
        raise NotImplementedError()
