class lista_enlazada:
    """Clase que implementa una lista enlazada"""
    class nodo:
      __slots__='element','next'
      def __init__(self,elemento,next) -> None:
         self.element=elemento
         self.next=next
         
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
      if self.is_empty():
        self.tail=new_nodo
      self.head=new_nodo
      self.size+=1
      
    def get_head(self)->nodo:
      return str(self.head.element)+' apunta hacia ->'+str(self.head.next.element)
    
    def get_tail(self)->nodo:
      return str(self.tail.element)
    
    def add_tail(self,elemento)->None:
      new_nodo=lista_enlazada.nodo(elemento,None)
      if self.is_empty():
        self.head=new_nodo
      else:
        self.tail.next=new_nodo
      self.tail=new_nodo
      self.size+=1
      
    def search(self,value)->nodo:
      """This method search a nodo in a linkedList 

      :param value: the value of the nodo to search
      :type value: any type
      :return: if the function find the value , return the nodo , but , if not , return None
      :rtype: nodo
      """
      current_nodo=self.head
      while current_nodo:
        if current_nodo.element==value:
          return current_nodo
        current_nodo=current_nodo.next
      return None
        
    def __str__(self) -> str:
      current_nodo=self.head
      cadena=''
      while current_nodo:
        cadena+=str(current_nodo.element)
        if current_nodo.next:
          cadena+=' -> '
        current_nodo=current_nodo.next
      return cadena
      
if __name__=='__main__':
  l1=lista_enlazada()
  print(l1.is_empty())
  l1.add_head(2)
  print(len(l1))
  l1.add_head(23)
  print(len(l1))
  l1.add_head(3444)
  l1.add_head(2000)
  l1.add_tail(21221)
  print(l1)
  print(l1.get_head())
  print(l1.get_tail())
  resultado=l1.search(12)
  resultado2=l1.search(23)
  print(resultado,resultado2.element,sep='  ')