from httplib import HTTPSConnection as Https

import prowlpy

class ProwlTestCase(TestCase):
    
    def setUp(self):
        """setup test"""
        # h = Https(API_DOMAIN)
        # h.request(  "POST",
        #             "/publicapi/add",
        #             headers = self.headers,
        #             body = urlencode(data))
        # response = h.getresponse()
        # request_status = response.status
        # self.mox.CreateMock(Https.request)
        # Https.request("api.prowlapp.com").AndReturn("")
        # self.mox.ReplayAll()

    def test_verify_key(self):
        """ This shows how to test helper classes' methods """
        

    def test_post(self):
        """Ensure post"""
        pass

    def test_retrieve_token(self):
        """Ensure token can be retrieved"""
        pass

    def test_retrieve_apikey(self):
        """Ensure API keys can be retrieved"""
        pass
