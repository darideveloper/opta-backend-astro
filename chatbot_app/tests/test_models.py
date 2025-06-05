from core.tests_base.test_models import TestchatbotAppModelsBase


class RespuestaTestCase(TestchatbotAppModelsBase):
    
    def setUp(self):
        # Create initial data
        self.create_respuesta()
        
    def test_titulo_clean_no_empty(self):
        pass
    
    def test_titulo_clean_with_empty(self):
        pass
    
    def test_submomento_str(self):
        pass
    