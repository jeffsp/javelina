'''
Jeff Perry <jeffsp@gmail.com>
version 1.0
2014-06-25
'''

import os
import javelina
import unittest
import tempfile

class RatexTestCase(unittest.TestCase):

    def setUp(self):
        javelina.app.config['TESTING'] = True
        javelina.app.config['WTF_CSRF_ENABLED'] = False
        self.app = javelina.app.test_client()

    def tearDown(self):
        pass

    def login(self, email, password):
        return self.app.post('/login', data=dict(login=email, password=password), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('admin@zetamon.com', 'asdfASDF1234')
        assert 'Logged in as:' in rv.data
        rv = self.logout()
        assert 'log in' in rv.data

    def test_get_authorization_code(self):
        assert (True)

    def test_get_access_token(self):
        assert (True)

if __name__ == '__main__':
    unittest.main()
