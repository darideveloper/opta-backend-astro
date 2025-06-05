from django.test import TestCase
from chatbot_app import models

from utils.media import get_test_file


class TestchatbotAppModelsBase(TestCase):
    """Base class for chatbot_app models tests."""

    def create_tipo_lead(self, nombre: str = "Test Tipo Lead") -> models.TipoLead:
        """Create a TipoLead instance for testing.

        Args:
            nombre (str, optional): The name of the TipoLead.
                Defaults to "Test Tipo Lead".

        Returns:
            models.TipoLead: The created TipoLead instance.
        """
        return models.TipoLead.objects.create(nombre=nombre)

    def create_programa(
        self, nombre: str = "Test Programa", tipo_lead: models.TipoLead = None
    ) -> models.Programa:
        """Create a Programa instance for testing.

        Args:
            nombre (str, optional): The name of the Programa.
                Defaults to "Test Programa".
            tipo_lead (models.TipoLead, optional): The TipoLead instance associated
                with the Programa. Defaults to None.

        Returns:
            models.Programa: The created Programa instance.
        """
        if tipo_lead is None:
            tipo_lead = self.create_tipo_lead()
        return models.Programa.objects.create(nombre=nombre, tipo_lead=tipo_lead)

    def create_momento(
        self, nombre: str = "Test Momento", programa: models.Programa = None
    ) -> models.Momento:
        """Create a Momento instance for testing.

        Args:
            nombre (str, optional): The name of the Momento.
                Defaults to "Test Momento".
            programa (models.Programa, optional): The Programa instance associated
                with the Momento. Defaults to None.

        Returns:
            models.Momento: The created Momento instance.
        """
        if programa is None:
            programa = self.create_programa()
        return models.Momento.objects.create(nombre=nombre, programa=programa)

    def create_submomento(
        self, nombre: str = "Test Submomento", momento: models.Momento = None
    ) -> models.Submomento:
        """Create a Submomento instance for testing.

        Args:
            nombre (str, optional): The name of the Submomento.
                Defaults to "Test Submomento".
            momento (models.Momento, optional): The Momento instance associated
                with the Submomento. Defaults to None.

        Returns:
            models.Submomento: The created Submomento instance.
        """
        if momento is None:
            momento = self.create_momento()
        return models.Submomento.objects.create(nombre=nombre, momento=momento)

    def create_documento(
        self,
        nombre: str = "Test Documento",
        archivo_name: str = "test.pdf",
        palabras_clave: list = ["test", "documento"],
    ) -> models.Documento:
        """Create a Documento instance for testing.

        Args:
            nombre (str, optional): The name of the Documento.
                Defaults to "Test Documento".
            archivo (str, optional): The file path of the Documento in media.
                Defaults to "test_documento.pdf".
            palabras_clave (list, optional): List of keywords
                associated with the Documento.
                Defaults to ["test", "documento"].

        Returns:
            models.Documento: The created Documento instance.
        """

        # Format kywords to tagify
        palabras_clave = map(
            lambda palabra_clave: {"value": palabra_clave}, palabras_clave
        )
        palabras_clave_str = f"[{','.join(map(str, palabras_clave))}]"

        # Get test file
        test_file = get_test_file(archivo_name)

        # Create documento instance
        return models.Documento.objects.create(
            nombre=nombre,
            archivo=test_file,
            palabras_clave=palabras_clave_str,
        )

    def create_respuesta(
        self,
        titulo: str = "Test Respuesta",
        contenido: str = "This is a test response.",
        image_name: str = "test_image.webp",
        prioridad: int = 1,
        submomento: models.Submomento = None,
        documento: models.Documento = None,
    ) -> models.Respuesta:
        """Create a Respuesta instance for testing.

        Args:
            titulo (str, optional): The title of the Respuesta.
                Defaults to "Test Respuesta".
            contenido (str, optional): The content of the Respuesta.
                Defaults to "This is a test response.".
            image_name (str, optional): The name of the image file
                associated with the Respuesta. Defaults to "test_image.webp".
            prioridad (int, optional): The priority of the Respuesta.
                Defaults to 1.
            submomento (models.Submomento, optional): The Submomento instance
                associated with the Respuesta. Defaults to None.
            documento (models.Documento, optional): The Documento instance
                associated with the Respuesta. Defaults to None.

        Returns:
            models.Respuesta: The created Respuesta instance.
        """
        if submomento is None:
            submomento = self.create_submomento()
        if documento is None:
            documento = self.create_documento()

        # Get test file for image
        image_file = get_test_file(image_name)

        return models.Respuesta.objects.create(
            titulo=titulo,
            contenido=contenido,
            image=image_file,
            prioridad=prioridad,
            submomento=submomento,
            documento=documento,
        )
