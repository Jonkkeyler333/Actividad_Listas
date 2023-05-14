class lista_enlazada:
    class nodo:
      __slots__='element','siguiente'
      def __init__(self,elemento,siguiente) -> None:
         self.element=elemento
         self.siguiente=siguiente
           
    def __init__(self) -> None:
       self.head=None
       self.tail=None
       self.size=0
    
    def __len__(self)->int:
      return self.size
    
    def is_empty(self)->bool:
      return  self.size==0
    
    def add_head(self,elemento)->None:
      new_nodo=lista_enlazada.nodo(elemento,self.head)
      if self.is_empty:
        self.tail=new_nodo
      self.head=new_nodo
      self.size+=1
    
    def add_tail(self,elemento)->None:
      new_nodo=lista_enlazada.nodo(elemento,None)
      if self.is_empty:
        self.head=new_nodo
      else:
        self.tail.siguiente=new_nodo
      self.tail=new_nodo
      self.size+=1
      
if __name__=='__main__':
  l1=lista_enlazada()
  print(l1.is_empty())
  l1.add_head(2)
  print(len(l1))
  l1.add_head(23)
  print(len(l1))
  
  
      
      