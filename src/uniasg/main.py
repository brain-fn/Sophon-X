# load Constants
from constants import *
# load recipes
from recipes import Recipes
# load utils
from utils import eval_recipe


# load ASG
import asg
for item in dir(asg):
    if not item.startswith("__"):
        Classes['core.'+item]=getattr(asg,item)

# load Config
try:
    from config import *

except:
    print "No config, defaulting to IMode"
    Mode = IMode

if Mode == IMode:
    init, root_interface = eval_recipe(('IMode',Recipes['IMode']))
else:
    raise NotImplementedError("Unknown Mode: "+Mode)

# init state
class state (object):
    Classes = Classes
    Inputs = Inputs
    Outputs = Outputs
    RootInterface = root_interface
    class config(object):
        plugins = Plugins

# Load plugins

import plugnplay
from plugins.interfaces import ExternalInterface
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
plugnplay.plugin_dirs = [dir_path+"/plugins/python/"]
plugnplay.load_plugins()

ExternalInterface.register(state)


if __name__ == "__main__":
    init._run()
else:
    # Setup some interfaces to run it from external programm
    pass