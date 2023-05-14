class Empty(Exception):
    def __init__(self,mensaje:str='La lista esta vacia') -> None:
        self.mensaje=mensaje
        super().__init__(self.mensaje)
    
    def __str__(self) -> str:
        return self.mensaje