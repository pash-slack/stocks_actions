import unittest
import stonks
import xmlrunner


class stonks_test(unittest.TestCase):

    def test_response_has_zip(self):
        sc = stonks.slackChecker('WORK')
        response = sc.get_latest_info()
        self.assertTrue('zip' in response)
        
    def test_intentionally_failing(self):
        self.assertTrue(False)

if __name__ == '__main__':
    print('Starting Kennel integration tests!')
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'), failfast=False)
