import json
from mock import patch
import os
from StringIO import StringIO
import shutil
import tempfile
from unittest import TestCase

from regulations.generator.api_reader import Client

class ClientTest(TestCase):
    def setUp(self):
        self.client = Client("http://example.com")
        Client._reg_cache = {}

    @patch('regulations.generator.api_reader.requests')
    def test_regulation(self, requests):
        to_return = {'example': 0}
        get = requests.get
        get.return_value.json.return_value = to_return
        self.assertEqual(to_return,
                self.client.regulation("label-here", "date-here"))
        self.assertTrue(get.called)
        param = get.call_args[0][0]
        self.assertTrue('http://example.com' in param)
        self.assertTrue('label-here' in param)
        self.assertTrue('date-here' in param)

    @patch('regulations.generator.api_reader.requests')
    def test_layer(self, requests):
        to_return = {'example': 1}
        get = requests.get
        get.return_value.json.return_value = to_return
        self.assertEqual(to_return, 
                self.client.layer("layer-here", "label-here", "date-here"))
        self.assertTrue(get.called)
        param = get.call_args[0][0]
        self.assertTrue('http://example.com' in param)
        self.assertTrue('layer-here' in param)
        self.assertTrue('label-here' in param)
        self.assertTrue('date-here' in param)

    @patch('regulations.generator.api_reader.requests')
    def test_notices(self, requests):
        to_return = {'example': 1}
        get = requests.get
        get.return_value.json.return_value = to_return
        self.assertEqual(to_return, self.client.notices())
        self.assertTrue(get.called)
        param = get.call_args[0][0]
        self.assertTrue('http://example.com' in param)

    @patch('regulations.generator.api_reader.requests')
    def test_notice(self, requests):
        to_return = {'example': 1}
        get = requests.get
        get.return_value.json.return_value = to_return
        self.assertEqual(to_return, self.client.notice("doc"))
        self.assertTrue(get.called)
        param = get.call_args[0][0]
        self.assertTrue('http://example.com' in param)
        self.assertTrue('doc' in param)

    def test_local_fs(self):
        """Verify that it's possible to host the files locally, where
        index.html is used in place of just the directory name."""
        tmp_root = tempfile.mkdtemp() + os.sep
        notice_path = tmp_root + os.sep + "notice" + os.sep
        os.mkdir(notice_path)
        with open(notice_path + "index.html", 'w') as f:
            f.write('{"results": ["example"]}')
        client = Client(tmp_root)
        results = client.notices()
        shutil.rmtree(tmp_root)
        self.assertEqual(["example"], results['results'])

    @patch('regulations.generator.api_reader.requests')
    def test_reg_cache(self, requests):
        child = {
            'text': 'child', 
            'children': [], 
            'label': ['923', 'a']
        }
        to_return = {
            'text': 'parent', 
            'label': ['923'],
            'children': [child]
        }
        get = requests.get
        get.return_value.json.return_value = to_return
        self.assertEqual(to_return, self.client.regulation('923', 'ver'))
        self.assertEqual(to_return, self.client.regulation('923', 'ver'))
        self.assertEqual(child, self.client.regulation('923-a', 'ver'))
        self.assertEqual(1, get.call_count)
        get.return_value.json.return_value = to_return
        self.client.regulation('923-b', 'ver')
        self.assertEqual(2, get.call_count)