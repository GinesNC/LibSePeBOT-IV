import unittest
from lib.dbgestion import DbGestion
import random

class Test(unittest.TestCase):
    global uid
    global tipo
    uid = random.randint(10000, 100000)
    tipo = random.choice(["libro", "pelicula", "serie"])

    def test_B_Insertar(self):

        data = DbGestion.crear_dato('test prueba', 2018, 10,tipo)

        self.assertTrue(DbGestion.insertarDatos(data,uid), "Inserccion incorrecta")


    def test_C_Modificar(self):
        tipo1 = random.choice(["libro", "pelicula", "serie"])
        titulo = "test prueba"
        new_datos = {'titulo': 'mod test prueba', 'año': 2017, 'puntuacion': 8, 'tipo':tipo1}

        self.assertTrue(DbGestion.modificarDatos(titulo, new_datos, uid), "Modificacion incorrecta")

    def test_D_UserActividad(self):
        #igual que antes pero se busca un uid
        self.assertGreaterEqual(DbGestion.userActividad(uid),1, "No tiene actividad")


    def test_E_Borrar(self):
        #igual pero para borrar dato

        titulo_borrar = "mod test prueba"

        self.assertTrue(DbGestion.eliminarDatos(titulo_borrar, uid), "Borrado incorrecto")




if __name__ == '__main__':
    unittest.main()
