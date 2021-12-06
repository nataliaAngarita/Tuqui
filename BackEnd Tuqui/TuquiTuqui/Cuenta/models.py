from django.db import models

# Creación de modelos CRUD.
class Perfil(models.Model):

    #Atributos
    nombres= models.CharField(max_length=50)
    apellidos= models.CharField(max_length=50)
    telefono= models.CharField(max_length=50)
    correo= models.CharField(max_length=100)
    contraseña= models.CharField(max_length=100)
    #metodos
    def _str_(Self):
       #define el nombre de como se identifica
       return Self.nombres

class TipoCarteraAhorro(models.Model):

    #Atributos
    idTipoCartera= models.CharField(max_length=2)
    TipoCartera=models.CharField(max_length=100)

    #metodos
    def __str__(self):
        return self.TipoCartera

class CarteraAhorro(models.Model):
    #Atributos
    idCuenta=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    fecha=models.DateTimeField()
    cantidad=models.IntegerField(null=True)
    TipoCartera=models.ForeignKey(TipoCarteraAhorro, on_delete=models.CASCADE)

    #metodos
    def __str__(self):
        return self.nombre
class Ingresos(models.Model):
    #Atributos
    descripcion=models.CharField(max_length=300)
    fecha=models.DateTimeField()
    valor=models.IntegerField()
    Cuenta=models.ForeignKey(CarteraAhorro,on_delete=models.CASCADE)

     #metodos
    def __str__(self):
        return self.descripcion

class TipoEgreso(models.Model):
    #Atributos
    idTipoEgreso=models.IntegerField()
    TipoEgreso=models.CharField(max_length=100)
    #metodos
    def __str__(self):
        return self.TipoEgreso

class Egreso (models.Model):
    #Atributos
    descripcion=models.CharField(max_length=300)
    fecha=models.DateTimeField()
    valor=models.IntegerField()
    Cuenta=models.ForeignKey(CarteraAhorro,on_delete=models.CASCADE)
    TipoEgreso=models.ForeignKey(TipoEgreso,on_delete=models.CASCADE)

     #metodos
    def __str__(self):
        return self.descripcion
