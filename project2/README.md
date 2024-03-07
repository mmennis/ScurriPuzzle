# Basic PostcodeVerifier Library

Simple module for verifying UK based postcodes.
Based on https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
This verifier chooses to use the simpler regular expression from the above site but has been tested at a basic level with the more complex regular expression that allows for special cases.

Usage is as you would expect
```python
from postcode_verifier import UKPostcodeVerifier

if UKPostcodeVerifier.isValidPostcode('EC1A 1BB'):
    print('Looks OK to me')
```

## Testing
Testing requires data driven testing library (ddt)
```
pip3 install ddt
```
or run the requirements.txt

Run test code as follows
```
python3 -m unittest discover tests
```

Comments:

This is a fairly simple implementation.  Using static methods seemed like the straightforward approach.
However if we wanted a more extensible solution I would probably look at a _Verifier_ factory class or method to which one passed in a country code and then got back a concrete _XXXVerifier_ object derived from the BaseVerifier class that was specific to that country.
```
verifier = PostcodeVerifierFacory.getVerifier('uk')
verifier.isValid(postcode) # verifier is an instance of UKPostcodeVerifier
```
This would allow us to extend to other countries location string very easily going forward.  Also it would be simple enough to add an options dictionary to allow configuring the verifier so that you could for example allow it to use the special cases regular expresion.
