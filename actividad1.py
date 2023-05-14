class lista_enlazada:
    class nodo:
      __slots__='element','siguiente'
      def __init__(self,elemento,siguiente:int) -> None:
         self.element=elemento
         self.siguiente=siguiente
           
    def __init__(self) -> None:
       self.head=None
       self.size=0
    
    def __len__(self)->int:
      return self.size
    
    def is_empty(self)->bool:
      return  self.size==0
    
    def add_head(self)->None:
      pass