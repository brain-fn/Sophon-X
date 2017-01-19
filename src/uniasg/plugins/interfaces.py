from plugnplay import Interface

class ExternalInterface(Interface):

  '''
    Called to register external interfaces
    like interface to Facebook
    register_func is callable with :FIXME parameters
  '''
  def register(self, state):
    pass