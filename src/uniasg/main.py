# load Constants
from constants import *

# load ASG
import asg
for item in dir(asg):
    if not item.startswith("__"):
        Classes['core.'+item]=getattr(asg,item)

# load Config
try:
    from config import *
except:
    print "No config, just make a RootInterface and connect to it ConsoleView"
    root_interface = Classes['core.Interface']('Root Interface',
                                               'Root Interface',
                                               {},{})
    root_view = Classes['core.ConsoleView']({
        'name': 'Root View',
        'object': root_interface
    })
    init = root_view

# init state
class state (object):
    Classes = Classes
    Inputs = Inputs
    Outputs = Outputs

# Load plugins

import plugnplay
from plugins.interfaces import ExternalInterface
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
plugnplay.plugin_dirs = [dir_path+"/plugins/python/"]
plugnplay.load_plugins()

ExternalInterface.register(state, root_interface.add_interface)


if __name__ == "__main__":
    init._run()
else:
    # Setup some interfaces to run it from external programm
    pass