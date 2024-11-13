import argparse

class InvalidIp(Exception):
    '''
    Exception raised by ValidIpAction to signify an invalid IP address
    '''
    def __init__(self, ipvalue):
        self.ip = ipvalue
    def __str__(self):
        return 'ERROR: Invalid IP: {0}'.format(self.ip)

class ValidIpAction(argparse.Action):
    '''
    A custom action, used in conjunction with argparse to validate an
    IP address.
    '''
    def validate_ip(self, ipvalue):
        '''
        Validate an IP address, generate exception if need be.
        '''

        try:
            numbers = [int(n) for n in ipvalue.split('.')]
            # print numbers, len(numbers)
            if len(numbers) != 4:
                raise InvalidIp(ipvalue)
            if len([n for n in numbers if 0<=n and n<=255]) != 4:
                raise InvalidIp(ipvalue)
            return ipvalue
        except BaseException:
            raise InvalidIp(ipvalue)

    def __call__(self, parser, namespace, values, option_string=None):
        if type(values) == list:
            setattr(namespace, self.dest, list(map(self.validate_ip, values)))
        else:
            setattr(namespace, self.dest, self.validate_ip(values))


