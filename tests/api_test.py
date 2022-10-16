import unittest
import sys

sys.path.append('../')

from main import app

headers = {"Content-Type": "application/json"}


class ApiCapacityTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_empty(self):
        # When
        response = self.app.get('/stack?capacity=true')
        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual({}, response.json)

    def test_post(self):
        # When
        response = self.app.post('/stack', headers=headers, data="{'capacity': 5}")
        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual({'msg': "Success"}, response.json)

    def test_get_posted_capacity(self):
        # When
        self.app.post('/stack', headers=headers, data="{'capacity': 5}")
        response = self.app.get('/stack?capacity=true')
        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual({'val': 5}, response.json)


class ApiPushTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.post('/stack', headers=headers, data="{'capacity': 2}")

    def test_first_push(self):
        # When
        response = self.app.put('/stack', headers=headers, data="{'val': 2}")
        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual({'val': 2}, response.json)

    def test_overflow(self):
        # When
        response1 = self.app.put('/stack', headers=headers, data="{'val': 2}")
        response2 = self.app.put('/stack', headers=headers, data="{'val': 1}")
        response3 = self.app.put('/stack', headers=headers, data="{'val': 3}")
        # Then
        self.assertEqual(200, response1.status_code)
        self.assertEqual({'val': 2}, response1.json)
        self.assertEqual(200, response2.status_code)
        self.assertEqual({'val': 1}, response2.json)
        self.assertEqual(200, response3.status_code)
        self.assertEqual({}, response3.json)


class ApiPopTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.post('/stack', headers=headers, data="{'capacity': 2}")
        self.app.put('/stack', headers=headers, data="{'val': 1}")
        self.app.put('/stack', headers=headers, data="{'val': 2}")

    def test_one_pop(self):
        # When
        response = self.app.delete('/stack')
        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual({'val': 2}, response.json)

    def test_pop_till_empty(self):
        # When
        response1 = self.app.delete('/stack')
        response2 = self.app.delete('/stack')
        response3 = self.app.delete('/stack')
        # Then
        self.assertEqual(200, response1.status_code)
        self.assertEqual({'val': 2}, response1.json)
        self.assertEqual(200, response2.status_code)
        self.assertEqual({'val': 1}, response2.json)
        self.assertEqual(200, response3.status_code)
        self.assertEqual({}, response3.json)


class ApiTopTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.post('/stack', headers=headers, data="{'capacity': 2}")
        self.app.put('/stack', headers=headers, data="{'val': 1}")

    def test_first_top(self):
        # When
        response = self.app.get('/stack')
        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual({'val': 1}, response.json)

    def test_top_pop_till_empty(self):
        # When
        response1 = self.app.get('/stack')
        response2 = self.app.delete('/stack')
        response3 = self.app.get('/stack')
        # Then
        self.assertEqual(200, response1.status_code)
        self.assertEqual({'val': 1}, response1.json)
        self.assertEqual(200, response2.status_code)
        self.assertEqual({'val': 1}, response2.json)
        self.assertEqual(200, response3.status_code)
        self.assertEqual({}, response3.json)


class ApiPrintTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.post('/stack', headers=headers, data="{'capacity': 2}")

    def test_print_all(self):
        # When
        self.app.put('/stack', headers=headers, data="{'val': 1}")
        self.app.put('/stack', headers=headers, data="{'val': 2}")
        response = self.app.get('/stack?all=true')
        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual([1, 2], response.json)

    def test_print_empty(self):
        # When
        response3 = self.app.get('/stack?all=true')
        # Then
        self.assertEqual(200, response3.status_code)
        self.assertEqual([], response3.json)


if __name__ == "__main__":
    unittest.main()
