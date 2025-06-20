from core.tests_base.test_admin import TestAdminSeleniumBase
from core.tests_base.test_models import TestChatbotAppModelsBase


class DocumentoAdminTestCaseLive(TestAdminSeleniumBase, TestChatbotAppModelsBase):
    """ Test Custom js for DocumentoAdmin """
    
    def setUp(self):
        """ Admin view base data """
        
        # Endpoint
        super().setUp(endpont="/admin/chatbot_app/documento")
        
        # Data
        self.keywords = ["test-1", "test-2", "test-3"]
        for _ in range(2):
            self.create_documento(
                palabras_clave=self.keywords,
            )
            
    def test_tagify(self):
        """ Test tagify tag loaded """
        
        # load first document details page
        self.set_page(f"{self.endpoint}/1/")
        
        selectors = {
            "tagify_tag": 'tag span'
        }
        
        # check tagify tag is loaded
        elems = self.get_selenium_elems(selectors)
        self.assertIsNotNone(elems["tagify_tag"])
        
        # Validate tag content
        self.assertIn(elems["tagify_tag"].text.strip(), self.keywords)
        
    