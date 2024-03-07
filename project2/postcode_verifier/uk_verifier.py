from postcode_verifier.base_verifier import BasePostcodeVerifier
import re

class UKPostcodeVerifier(BasePostcodeVerifier):

    def isValidPostcode(pc):
        if not pc:
            return False
        #  Convert to upper case, trim and check for space
        postcode = pc.upper().strip()
        if not ' ' in postcode:
            return False
        # Replace instances of multiple spaces and check length
        multi_space = r"\s+"
        test_postcode = re.sub(multi_space, " ", postcode)
        if len(test_postcode) < 6 or len(test_postcode) > 8:
            return False
        #  Verify with official pattern for UK from website
        pattern = r"^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$"
        match = re.search(pattern, test_postcode)
        if match:
            return True
        else:
            return False
