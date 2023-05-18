from empty import Empty
class lista_enlazada:
    """Clase que implementa una lista enlazada"""
    class nodo:
      """Clase que implementa un nodo
      """
      __slots__='element','next'
      def __init__(self,elemento:any,next:any) -> None:
        """constructor of the class 'nodo'

        :param elemento: the element to save into the information field of the nodo
        :type elemento: any 
        :param next: pointer to point to the next element in the list
        :type next: any
        """
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
      if self.is_empty():
        raise Empty
      return str(self.head.element)+' apunta hacia ->'+str(self.head.next.element)
    
    def get_tail(self)->nodo:
      if self.is_empty():
        raise Empty
      return str(self.tail.element)
    
    def add_tail(self,elemento)->None:
      new_nodo=lista_enlazada.nodo(elemento,None)
      if self.is_empty():
        self.head=new_nodo
      else:
        self.tail.next=new_nodo
      self.tail=new_nodo
      self.size+=1
      
    def search(self,value:any)->nodo:
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
    
    def add(self,element:any)->None:
      new_nodo=lista_enlazada.nodo(element)
      pass
    
    def delete_head(self)->None:
      if self.is_empty():
        raise Empty
      self.size-=1
      self.head=self.head.next
    
    def pop(self)->nodo:
      if self.is_empty():
        raise Empty
      self.size-=1
      nodo=self.head
      self.head=self.head.next
      return nodo
    
    def delete_tail(self)->None:
      if self.is_empty():
        raise Empty
      current_nodo=self.head
      while current_nodo.next != self.tail:
        current_nodo=current_nodo.next
      current_nodo.next=None
      self.tail=current_nodo
      self.size-=1
      
    def delete(self,element:any)->nodo:
      if self.is_empty():
        raise Empty
      elif self.search(element)==None:
        return 'No se encontró el Nodo'
      elif self.head.element==element:
        return self.pop()
      elif self.tail.element==element:
        aux=self.tail
        self.delete_tail()
        return aux
      current_nodo=self.head
      while current_nodo.element != element:
        aux=current_nodo
        borr=current_nodo.next
        current_nodo=current_nodo.next
      aux.next = borr.next
      self.size-=1
      return borr
      
    def __str__(self) -> str:
      if self.is_empty():
        return None
      current_nodo=self.head
      cadena=''
      while current_nodo:
        cadena+=str(current_nodo.element)
        if current_nodo.next:
          cadena+=' -> '
        current_nodo=current_nodo.next
      return cadena
      
if __name__=='__main__':
  """Pruebas de la clase"""
  l1=lista_enlazada()
  print(l1.is_empty())
  ##probando la excepción
  try:
    l1.delete_head()
  except Empty:
    print('excepción exitosa')
    pass
  ##agregar a la cabeza de la lista
  l1.add_head(2)
  l1.add_head(23)
  l1.add_head('keyler')
  l1.add_head(3444)
  l1.add_head(2000)
  l1.add_tail(21221)
  print(l1)
  print('obteniendo la cabeza',l1.get_head())
  print('obteniendo la cola',l1.get_tail())
  resultado=l1.search(12)
  resultado2=l1.search(23)
  print(resultado,resultado2.element,sep='  ')
  print('tamaño de la lista',len(l1))
  ##eliminando elementos
  l1.delete_head()
  print('elimine la cabeza , ahora el tamaño de la lista',len(l1))
  print(l1)
  l1.delete_tail()
  print(l1)
  nodoe=l1.delete('keyler')
  print(l1,' //elemento eliminado = ',nodoe.element)
  l1.delete(2)
  print(l1,'// elemento eliminado 2')
  print(l1,'tamaño actual',len(l1))