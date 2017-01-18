import plugnplay
from plugins.interfaces import ExternalInterface



class PluginVKInterface(plugnplay.Plugin):
    implements = [ExternalInterface]

    def setup(self, interface_cls, action_cls):

        class PrintAction(action_cls):
            def do(self):
                print self.name
        OopsAction = PrintAction('Oops')

        VKInterface = interface_cls(name='VK Interface',
                                    actions={'ooops':OopsAction})
        return VKInterface

    def register(self,state,register_func):
        register_func('VK', self.setup(state.Classes['core.Interface'],
                                       state.Classes['core.Action']))

