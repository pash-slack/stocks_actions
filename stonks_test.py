import unittest
import stonks
import xmlrunner


class stonks_test(unittest.TestCase):

    def test_response_has_zip(self):
        sc = stonks.slackChecker('WORK')
        response = sc.get_latest_info()
        self.assertTrue('zip' in response)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'), failfast=False)
