from src.Simple_Localizer import Simple_Localizer
from src.abc_base import BASE_Localizer


def test():
    print 'Subclass:', issubclass(Simple_Localizer, BASE_Localizer)
    print 'Instance:', isinstance(Simple_Localizer(), BASE_Localizer)

    for sc in BASE_Localizer.__subclasses__():
        print sc.__name__

if __name__ == '__main__':

  localizer = Simple_Localizer()

