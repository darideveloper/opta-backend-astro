from core.tests_base.test_models import TestChatbotAppModelsBase


class RespuestaTestCase(TestChatbotAppModelsBase):

    def setUp(self):
        # Create initial data
        self.respuesta = self.create_respuesta()

    def test_titulo_clean_no_empty(self):
        """Test that titulo_clean returns the title if it is not empty."""

        # Validate titulo_clean
        self.assertEqual(self.respuesta.titulo_clean, self.respuesta.titulo)

    def test_titulo_clean_empty(self):
        """Test that titulo_clean returns 'Respuesta' if the title is empty."""

        # Set title to empty string
        self.respuesta.titulo = ""
        self.respuesta.save()

        # Validate titulo_clean
        self.assertEqual(self.respuesta.titulo_clean, "Sin Título")

    def test_submomento_str(self):
        """Test that submomento_str returns the correct string representation."""

        # Validate string representation
        self.assertIn(
            self.respuesta.submomento.nombre,
            self.respuesta.submomento_str
        )
        self.assertIn(
            "Respuesta al submomento: ",
            self.respuesta.submomento_str
        )
