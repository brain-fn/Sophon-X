'''
Created on Aug 4, 2016

@author: keeper
'''
import types
from functools import partial
from pprint import pprint


class ProgHeader:
    ''' Program Header '''

    def __init__(self, obj={}):
        self.name = obj.get('name', 'n/a')
        self.description = obj.get('description', 'n/a')
        self.version = obj['version']
        self.scope = obj.get('scope', {})


class Container:
    ''' Contains other Data and provides access navigation '''

    def __init__(self, obj={}):
        self.name = obj.get('name', 'n/a')
        self.scope = obj.get('scope', {})
        self.views = obj.get('views', {})

class Action(object):
    def __init__(self, name, do=None):
        self.name = name
        #do = kwargs.get('do',None)
        if do:
            self.do = types.MethodType(do,self)

    def do(self):
        print "Doing Action: ", self.name

class Interface(object):

    def __init__(self, name,
                 descr = None,
                 # For some reason if make nav={} this {} will be shared between instances
                 nav = None,
                 actions = None):
        self.name = name
        self.description = descr or "No Description"
        self.nav = nav or dict()
        self.actions = actions or dict()
        if actions:
            assert all([isinstance(action,Action) for name, action in actions.items()]), \
                "Not all provided actions is instances of Action class"

    def add_interface(self,name,interface):
        assert isinstance(interface,self.__class__)
        l = (id(self.nav),id(interface.nav))
        self.nav[name]=interface
        l = (id(self.nav),id(interface.nav))
        print name

    def make_alias(self,name,ref):
        assert isinstance(ref,Action)
        self.actions[name] = ref


class View(object):
    ''' Information for building view to make beter handle of containers data scope '''

    def __init__(self,
                 name='n/a',
                 descr='No Description',
                 obj=None):
        self.name = name
        self.descr = descr
        self._obj = obj


class ConsoleView (View):
    actions ={}
    _summed_actions = {}
    _current_action = None

    def _update_actions(self):
        self._summed_actions = self.actions.copy()
        if self._obj.actions:
            self._summed_actions.update(self._obj.actions)

    def _run(self):
        while self._current_action != 'exit':
            print "\nView name: ", self.name
            obj = self._obj
            print obj, type(obj)
            if isinstance(obj,Interface):
                print "Interface name: ", obj.name,'\n'
                print "Navigation ( 'nav [name]' ):"
                for n,x in obj.nav.items():
                    print "\t",n
            print "Actions:"
            for n in self._summed_actions:
                print "\t",n
            action = raw_input(': ')
            if action not in self._summed_actions.keys():
                print "Wrong Action!"
            self._summed_actions[action].do()

    def __init__(self, *args, **kwargs):
        super(ConsoleView,self).__init__(*args, **kwargs)


        def _action_exit_do():
            print 'Exiting...'
            self._current_action = 'exit'

        self.action_exit = Action('Exit')
        self.action_exit.do = _action_exit_do

        def _action_nav_do(self,view):
            nav_to = raw_input("Choose nav object\n\t: ")
            if nav_to not in view._obj.nav.keys():
                print "Wrong Object!"
            else:
                print 'nav_to ', nav_to
                view._obj = view._obj.nav[nav_to]
                view._update_actions()
        self.action_nav = Action('Navigate',
                            do=partial(_action_nav_do, view=self))
        self.actions['exit'] = self.action_exit
        self.actions['nav'] = self.action_nav
        self._update_actions()


class DataField:
    pass

class URLLink:
    def __init__(self,obj={}):
        pass
        
