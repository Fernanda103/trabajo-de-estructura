class Cargo:
  secuencia=2
  cargos = [{"codigo":1,"cargo":"Gerente"}, {"codigo":2,"cargo":"Jefa"}]
  def __init__(self, cargo):
    Cargo.secuencia += 1
    self.codigo = Cargo.secuencia
    self.descripcion = cargo
  def  registro(self):
    return {"codigo":self.codigo,"cargo":self.descripcion}
    