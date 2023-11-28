import unittest
from io import StringIO
from unittest.mock import patch
from controlador import buscar_documento, buscar_carpeta
from json_functions import cargar_desde_json

class TestBuscarDocumento(unittest.TestCase):

    def test_buscar_documento(self):
        # Cargar el composite desde un archivo JSON (como explorador en tu caso)
        archivo_json = "Ejercicio_3(Samur)/tests.json"
        composite = cargar_desde_json(archivo_json)

        # Configurar la entrada del usuario para simular la entrada "se"
        with patch('builtins.input', side_effect=["se"]):
            # Capturar la salida estándar para evaluarla
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                buscar_documento(composite, "se")

        # Obtener la salida generada por la función
        output = mock_stdout.getvalue()

        # Verificar que la salida coincide con el resultado esperado
        self.assertIn("Documento: settings.txt, Tipo: Texto, Tamaño: 10 KB", output)
        self.assertIn("Documento: settings_wheel.jpg, Tipo: Imagen, Tamaño: 50 KB", output)
        self.assertIn("Documento: settings.txt, Tipo: Texto, Tamaño: 10 KB", output)
        self.assertIn("Documento: settings_wheel.jpg, Tipo: Imagen, Tamaño: 50 KB", output)

class TestBuscarCarpeta(unittest.TestCase):

    def test_buscar_carpeta(self):
        # Cargar el composite desde un archivo JSON (como explorador en tu caso)
        archivo_json = "Ejercicio_3(Samur)/tests.json"
        composite = cargar_desde_json(archivo_json)

        # Configurar la entrada del usuario para simular la entrada "config"
        with patch('builtins.input', side_effect=["config"]):
            # Capturar la salida estándar para evaluarla
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                buscar_carpeta(composite, "config")

        # Obtener la salida generada por la función
        output = mock_stdout.getvalue()

        # Verificar que la salida coincide con el resultado esperado
        self.assertIn("Carpeta: config", output)
        self.assertIn("  Archivo: settings.txt", output)
        self.assertIn("  Archivo: settings_wheel.jpg", output)
        self.assertIn("  Enlace: configLink (/ConfigGeneral/settings.txt)", output)


if __name__ == '__main__':
    unittest.main()