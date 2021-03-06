import unittest
from lib.dbgestion import DbGestion
import random
import json
import lib.rutas as rutas

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


    def test_Index(self):
        self.assertGreaterEqual(json.loads(rutas.index())['status'],"OK", "No OK.")

    def test_F_status(self):
        req = rutas.status()
        j = json.loads(req)
        self.assertGreaterEqual(j['status'],"OK", "No OK.")

    def test_G_datos(self):
        self.assertGreaterEqual(json.loads(rutas.datos())['status'],"OK", "No OK.")

    def test_H_insertdatos(self):
        self.assertGreaterEqual(json.loads(rutas.insertardatos())['status'],"OK", "No OK.")



if __name__ == '__main__':
    unittest.main()
