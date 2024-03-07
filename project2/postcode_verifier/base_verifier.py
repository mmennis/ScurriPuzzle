from abc import ABC, abstractmethod

# Other verifier classes should extend this BaseVerifier
# Could be useful if we decide to add to the verifier interface
class BasePostcodeVerifier(ABC):

    @abstractmethod
    def isValidPostcode(postcode):
        pass
