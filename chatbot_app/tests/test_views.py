from chatbot_app import models

from core.tests_base.test_views import ViewsBaseTestCase
from core.tests_base.test_models import TestChatbotAppModelsBase


class TipoLeadViewSetTestCase(ViewsBaseTestCase, TestChatbotAppModelsBase):

    def setUp(self):
        """
        Set up the test case with initial data and endpoint.
        """
        super().setUp("/api/demo/tipolead/")

        # Create initial data
        self.tipo_lead = self.create_tipo_lead()

    def test_get_single(self):
        """
        Test retrieving a single TipoLead instance.
        """

        # get data and validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

        # check response length
        self.assertEqual(len(response.data), 1)

        # validate the data of the first TipoLead
        tipolead_data = response.data[0]
        self.assertEqual(tipolead_data["id"], self.tipo_lead.id)
        self.assertEqual(tipolead_data["nombre"], self.tipo_lead.nombre)

    def test_get_many(self):
        """
        Test retrieving multiple TipoLead instances.
        """

        self.create_tipo_lead("tipo lead b")
        self.create_tipo_lead("tipo lead c")

        # get data and validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

        # check response length
        self.assertEqual(len(response.data), 3)

        # validate the data of the each TipoLead
        result_data = response.data
        for result in result_data:
            tipo_lead_instance = models.TipoLead.objects.get(id=result["id"])
            self.assertIsNotNone(tipo_lead_instance)
            self.assertEqual(result["nombre"], tipo_lead_instance.nombre)

    def test_get_no_data(self):
        """
        Test retrieving no TipoLead instances.
        """

        # delete the created TipoLead
        self.tipo_lead.delete()

        # get data and validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

        # check response length
        self.assertEqual(len(response.data), 0)


class ProgramaViewSetTestCase(ViewsBaseTestCase, TestChatbotAppModelsBase):

    def setUp(self):
        """
        Set up the test case with initial data and endpoint.
        """
        super().setUp("/api/demo/programa/")

        # Create initial data
        self.tipo_lead = self.create_tipo_lead("tipo lead a")
        self.programa = self.create_programa(tipo_lead=self.tipo_lead)

    def test_get_single(self):
        """
        Test retrieving a single Programa instance.
        """

        # get data and validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

        # check response length
        self.assertEqual(len(response.data), 1)

        # validate the data of the first Programa
        programa_data = response.data[0]
        self.assertEqual(programa_data["id"], self.programa.id)
        self.assertEqual(programa_data["nombre"], self.programa.nombre)
        self.assertEqual(programa_data["tipo_lead"], self.tipo_lead.id)

    def test_get_many(self):
        """
        Test retrieving multiple TipoLead instances.
        """

        self.create_programa("programa b", tipo_lead=self.tipo_lead)
        self.create_programa("programa c", tipo_lead=self.tipo_lead)

        # get data and validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

        # check response length
        self.assertEqual(len(response.data), 3)

        # validate the data of the each Programa
        result_data = response.data
        for result in result_data:
            programa_instance = models.Programa.objects.get(id=result["id"])
            self.assertIsNotNone(programa_instance)
            self.assertEqual(result["nombre"], programa_instance.nombre)
            self.assertEqual(result["tipo_lead"], programa_instance.tipo_lead.id)

    def test_get_no_data(self):
        """
        Test retrieving no Programa instances.
        """

        # delete the created Programa
        self.programa.delete()

        # get data and validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

        # check response length
        self.assertEqual(len(response.data), 0)


class MomentoViewSetTestCase(ViewsBaseTestCase, TestChatbotAppModelsBase):

    def setUp(self):
        """
        Set up the test case with initial data and endpoint.
        """
        super().setUp("/api/demo/momento/")

        # Create initial data
        self.programa = self.create_programa()
        self.momento = self.create_momento(programa=self.programa)

    def test_get_single(self):
        """
        Test retrieving a single Momento instance.
        """

        # get data and validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

        # check response length
        self.assertEqual(len(response.data), 1)

        # validate the data of the first Momento
        momento_data = response.data[0]
        self.assertEqual(momento_data["id"], self.momento.id)
        self.assertEqual(momento_data["nombre"], self.momento.nombre)
        self.assertEqual(momento_data["programa"], self.programa.id)

    def test_get_many(self):
        """
        Test retrieving multiple Momento instances.
        """

        self.create_momento("momento b", programa=self.programa)
        self.create_momento("momento c", programa=self.programa)

        # get data and validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

        # check response length
        self.assertEqual(len(response.data), 3)

        # validate the data of the each Momento
        result_data = response.data
        for result in result_data:
            momento_instance = models.Momento.objects.get(id=result["id"])
            self.assertIsNotNone(momento_instance)
            self.assertEqual(result["nombre"], momento_instance.nombre)
            self.assertEqual(result["programa"], momento_instance.programa.id)

    def test_get_no_data(self):
        """
        Test retrieving no Momento instances.
        """

        # delete the created Momento
        self.momento.delete()

        # get data and validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

        # check response length
        self.assertEqual(len(response.data), 0)


class SubmomentoViewSetTestCase(ViewsBaseTestCase, TestChatbotAppModelsBase):

    def setUp(self):
        """
        Set up the test case with initial data and endpoint.
        """
        super().setUp("/api/demo/submomento/")

        # Create initial data
        self.momento = self.create_momento()
        self.submomento = self.create_submomento(momento=self.momento)

    def test_get_single(self):
        """
        Test retrieving a single Submomento instance.
        """

        # get data and validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

        # check response length
        self.assertEqual(len(response.data), 1)

        # validate the data of the first Submomento
        submomento_data = response.data[0]
        self.assertEqual(submomento_data["id"], self.submomento.id)
        self.assertEqual(submomento_data["nombre"], self.submomento.nombre)
        self.assertEqual(submomento_data["momento"], self.momento.id)

    def test_get_many(self):
        """
        Test retrieving multiple Submomento instances.
        """

        self.create_submomento("submomento b", momento=self.momento)
        self.create_submomento("submomento c", momento=self.momento)

        # get data and validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

        # check response length
        self.assertEqual(len(response.data), 3)

        # validate the data of each Submomento
        result_data = response.data
        for result in result_data:
            submomento_instance = models.Submomento.objects.get(id=result["id"])
            self.assertIsNotNone(submomento_instance)
            self.assertEqual(result["nombre"], submomento_instance.nombre)
            self.assertEqual(result["momento"], submomento_instance.momento.id)

    def test_get_no_data(self):
        """
        Test retrieving no Submomento instances.
        """

        # delete the created Submomento
        self.submomento.delete()

        # get data and validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

        # check response length
        self.assertEqual(len(response.data), 0)


class RespuestaViewSetTestCase(ViewsBaseTestCase, TestChatbotAppModelsBase):

    def setUp(self):
        """
        Set up the test case with initial data and endpoint.
        """
        super().setUp("/api/demo/respuesta/")

        # Create initial data
        self.submomento = self.create_submomento()
        self.respuesta = self.create_respuesta(
            "respuesta a", "response content a", prioridad=1, submomento=self.submomento
        )

    def test_get_single(self):
        """
        Test retrieving a single Respuesta instance.
        """

        # get data and validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

        # check response length
        self.assertEqual(len(response.data), 1)

        # validate the data of the first Respuesta
        respuesta_data = response.data[0]
        self.assertEqual(respuesta_data["id"], self.respuesta.id)
        self.assertEqual(respuesta_data["titulo"], self.respuesta.titulo)
        self.assertEqual(respuesta_data["contenido"], self.respuesta.contenido)
        self.assertIn(self.respuesta.image.url, respuesta_data["image"])
        self.assertEqual(respuesta_data["prioridad"], self.respuesta.prioridad)
        self.assertEqual(respuesta_data["submomento"], self.submomento.id)
        self.assertEqual(respuesta_data["documento"]["id"], self.respuesta.documento.id)

    def test_get_many(self):
        """
        Test retrieving multiple Respuesta instances.
        """

        self.create_respuesta(
            "respuesta b", "response content b", prioridad=2, submomento=self.submomento
        )
        self.create_respuesta(
            "respuesta c", "response content c", prioridad=3, submomento=self.submomento
        )

        # get data and validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

        # check response length
        self.assertEqual(len(response.data), 3)

        # validate the data of each Respuesta
        result_data = response.data
        for result in result_data:
            respuesta_instance = models.Respuesta.objects.get(id=result["id"])
            self.assertIsNotNone(respuesta_instance)
            self.assertEqual(result["titulo"], respuesta_instance.titulo)
            self.assertEqual(result["contenido"], respuesta_instance.contenido)
            self.assertIn(respuesta_instance.image.url, result["image"])
            self.assertEqual(result["prioridad"], respuesta_instance.prioridad)
            self.assertEqual(result["submomento"], respuesta_instance.submomento.id)
            self.assertEqual(result["documento"]["id"], respuesta_instance.documento.id)

    def test_get_no_data(self):
        """
        Test retrieving no Respuesta instances.
        """

        # delete the created Respuesta
        self.respuesta.delete()

        # get data and validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

        # check response length
        self.assertEqual(len(response.data), 0)


class DocumentoViewSetTestCase(ViewsBaseTestCase, TestChatbotAppModelsBase):

    def setUp(self):
        """
        Set up the test case with initial data and endpoint.
        """
        super().setUp("/api/demo/documento/")

        # Create initial data
        self.documento = self.create_documento()

    def test_get_single_no_keywords(self):
        """
        Test try to retrive a single Documento instance.
        Expect no data to be returned.
        """
        
        # get data and validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

        # check response length
        self.assertEqual(len(response.data), 0)
        
    def test_get_single_keywords(self):
        """
        Test try to retrive a single Documento instance.
        Expect no data to be returned.
        """
        
        # get data and validate response submiting query parameters
        response = self.client.get(self.endpoint, {"tags": "test,documento"})
        self.assertEqual(response.status_code, 200)

        # check response length
        self.assertEqual(len(response.data), 1)

        # validate the data of the first Documento
        documento_data = response.data[0]
        self.assertEqual(documento_data["id"], self.documento.id)
        self.assertEqual(documento_data["nombre"], self.documento.nombre)
        self.assertIn(self.documento.archivo.url, documento_data["archivo"])

    def test_get_many(self):
        """
        Test retrieving multiple Documento instances.
        """

        self.create_documento(
            palabras_clave=["b", "documento"],
        )
        self.create_documento(
            palabras_clave=["c", "documento"],
        )
        
        # get data and validate response
        response = self.client.get(self.endpoint, {"tags": "test,documento"})
        self.assertEqual(response.status_code, 200)

        # check response length
        self.assertEqual(len(response.data), 3)

        # validate the data of each Documento
        result_data = response.data
        for result in result_data:
            documento_instance = models.Documento.objects.get(id=result["id"])
            self.assertIsNotNone(documento_instance)
            self.assertEqual(result["nombre"], documento_instance.nombre)

    def test_get_no_data(self):
        """
        Test retrieving no Documento instances.
        """

        # delete the created Documento
        self.documento.delete()

        # get data and validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

        # check response length
        self.assertEqual(len(response.data), 0)
