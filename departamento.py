class Departamento:
  secuencia=1
  departamentos = [{"departamento":1, "nombre":"Recursos Humanos" }]
  def __init__(self, descrip):
    Departamento.secuencia +=1
    self.codigo = Departamento.secuencia
    self.departamento = descrip
  def  registro(self):
    return {"departamento": self.codigo, "nombre": self.departamento}
