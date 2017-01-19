import plugnplay
from plugins.interfaces import ExternalInterface
from vk import API,AuthSession



class PluginVKInterface(plugnplay.Plugin):
    implements = [ExternalInterface]

    def setup(self, state):
        classes = state.Classes
        config = state.config.plugins['VK']

        class PrintAction(classes['core.Action']):
            def do(self):
                print self.name
        OopsAction = PrintAction('Oops')

        class PostAction(classes['core.Action']):
            '''
                Proper semantic action that uses Message object
            '''
            def do(self, msg):
                assert isinstance(msg,classes['core.Message'])
                raise NotImplementedError

        class ExperimentalWallPost(classes['core.Action']):
            ''' Just asks for a text and posts it to
                current wall or the one in the config'''
            def do(self):
                pass

        class VKInterface(classes['core.Interface']):
            def __init__(self, config, wall=None):
                super(VKInterface,self).__init__(name='VK Interface',
                                                 descr='Interface to VK.com')
                session = AuthSession(scope='wall',
                                         app_id=config['app_id'],
                                         user_login=config['user_login'],
                                         user_password=config['user_password'])

                API.access_token=config['access_token']
                self._vkapi = API(session=session)
                self.actions = {
                    'ooops'   : OopsAction,
                    'wallpost': ExperimentalWallPost
                }
        return VKInterface(config)

    def register(self,state):
        state.RootInterface.add_interface(
            'VK', self.setup(state))

