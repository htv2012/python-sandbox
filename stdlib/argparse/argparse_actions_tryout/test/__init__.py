import argparse
import unittest
import argparse_actions2 as argparse_actions

class ValidateIpActionSingleArgumentTest(unittest.TestCase):
    #
    # Support
    #
    def setUp(self):
        self.parser = argparse.ArgumentParser(description='Custom Actions')
        self.parser.add_argument('ip', action=argparse_actions.ValidIpAction)
    
    def perform_with_exception(self, command_line):
        self.assertRaises(
            argparse_actions.InvalidIp,
            self.parser.parse_args, 
            command_line)

    #
    # The tests
    #
    def single_valid_test(self):
        command_line = ['10.93.255.134']
        options = self.parser.parse_args(command_line)
        self.assertEqual(options.ip, command_line[0])
        
    def non_number_test(self):
        self.perform_with_exception(['10.93.foo.25'])
        
    def too_few_numbers_test(self):
        self.perform_with_exception(['10.93.25'])
        
    def too_many_numbers_test(self):
        self.perform_with_exception(['10.93.25.43.195'])

class ValidIpActionMultipleArgumentsTest(unittest.TestCase):
    #
    # Support
    #
    def setUp(self):
        self.parser = argparse.ArgumentParser(description='Custom Actions')
    
    def perform_with_exception(self, command_line):
        self.parser.add_argument(
            'ip', 
            nargs=len(command_line),
            action=argparse_actions.ValidIpAction)

        self.assertRaises(
            argparse_actions.InvalidIp,
            self.parser.parse_args, 
            command_line)

    #
    # The tests
    #
    def two_ip_test(self):
        self.parser.add_argument(
            'ip', 
            nargs=2,
            action=argparse_actions.ValidIpAction)
        command_line = ['10.93.25.78', '192.168.1.7']
        options = self.parser.parse_args(command_line)
        self.assertEqual(command_line, options.ip)
        
    def test1(self):
        command_line = ['10.0.1.8', '1.2.3.999']
        self.perform_with_exception(command_line)
        
    def test2(self):
        command_line = ['10.0.1.foo', '1.2.3.999']
        self.perform_with_exception(command_line)
