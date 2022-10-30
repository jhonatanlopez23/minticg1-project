from abc import ABCMeta, ABCMeta
class Abstract(metaclass=ABCMeta):
    _id: None
    
    def __init__(self, _id):
        """
        Crear el modelo 
        """
        self._id= _id