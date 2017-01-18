# Global Vars
Classes = {}
Inputs = []
Outputs = []

# Constants
class ASGConstant(object):
    def __init__(self, descr='No descr'):
        self.descr = descr

XRayMode = ASGConstant("'Browse' (non interactive) mode")
IMode = ASGConstant("Interactive mode")