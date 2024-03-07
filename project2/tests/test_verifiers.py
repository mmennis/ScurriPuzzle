import unittest
from ddt import ddt, data, unpack
from postcode_verifier import UKPostcodeVerifier

@ddt
class TestUKPostcodeVerifier(unittest.TestCase):

    @data(
        ('XXX', False, 'Totally bogus passed'),
        ('', False, 'Empty postcode passed'),
        (None, False, "Null object passed"),
        ('x910XA3', False, 'No space passed'),
        ('WE56   A1BB', False, 'Too long passed'),
        ('M1 1T', False, "Too short passed"),
        ('DN555 6X', False, 'Outward too long passed'),
        ('D999 AA', False, 'Invalid Outward passed'),
        ('E11A 1BB', False, 'Invalid Outward passed'),
        ('M1 87TH', False, 'Inward too long passed'),
        ('CR2 T7J', False, 'Invalid Inward passed'),
        ('CR2 7J8', False, 'Invalid Inward passed'),
        (' EC1A 1BB', True, 'Official example fails - useless space'),
        ('EC1A 1BB ', True, 'Official example fails - useless space'),
        ('EC1A   1BB', True, 'Official example fails - multi-spaces'),
        ('EC1A 1bb', True, 'Official example fails - lowercase'),
        ('EC1A 1BB', True, 'Official example fails'),
        ('W1A 0AX', True, 'Official example fails'),
        ('M1 1AE', True, 'Official example fails'),
        ('B33 8TH', True, 'Official example fails'),
        ('CR2 6XH', True, 'Official example fails'),
        ('DN55 1PT', True, 'Official example fails')
    )
    @unpack
    def test_postcode(self, postcode, expected, message):
        result = UKPostcodeVerifier.isValidPostcode(postcode)
        self.assertEqual(result, expected, message)

if __name__ == '__main__':
    unittest.main()
