from plugins.interfaces import ExternalInterface
import plugnplay


VKInterface = Clasess['core.Interface'](name='VK Interface')

print 'OLOOOOOOOOOOOOO'
class PluginVKInterface(plugnplay.Plugin):
    implements = [ExternalInterface]

    def register(self,register_func):
        register_func('VK',VKInterface)

