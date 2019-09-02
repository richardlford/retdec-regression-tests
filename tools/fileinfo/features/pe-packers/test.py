from regression_tests import *

class Test_SafeDisc(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            'sample_safedisc_001.dat',
            'sample_safedisc_002.dat',
            'sample_safedisc_003.dat',
        ],
        args='--json'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertTrue((self.fileinfo.output['tools'][1]['name'] == 'SafeDisc') or (self.fileinfo.output['tools'][2]['name'] == 'SafeDisc'))

class Test_SecuROM(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            'sample_securom_001.dat',
            'sample_securom_002.dat',
            'sample_securom_003.dat',
        ],
        args='--json'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'SecuROM')

class Test_StarForce(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            'sample_starforce_001.dat',
            'sample_starforce_002.dat',
            'sample_starforce_003.dat',
        ],
        args='--json'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertTrue('StarForce' in self.fileinfo.output['tools'][0]['name'])