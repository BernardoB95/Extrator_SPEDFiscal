from importlib import import_module
from inspect import getmembers, isabstract, isclass
from Core import IFactory


def load_factory(factory_name):
    """
    The Factory Pattern loader will receive the name of the factory to be instantiated.

    :param factory_name: Name of the factory to be instantiated
    :type factory_name: String
    :return: The factory to be instantiated
    :rtype: Class
    """

    try:
        block = factory_name[0]
        module = 'Core.Block_' + block + '.R' + factory_name + '_Factory'
        factory_module = import_module(module, 'Core')
    except ImportError:
        factory_module = import_module('Core.Null_Factory', 'Core')

    classes = getmembers(factory_module,
                         lambda m: isclass(m) and not isabstract(m))

    for name, _class in classes:
        if issubclass(_class, IFactory):
            return _class()
