'''
Created on Aug 4, 2016

@author: keeper
'''


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

class Action:
    def __init__(self):
        pass

class Interface(object):

    def __init__(self, name,
                 descr,
                 nav,
                 actions):
        self.name = name
        self.description = descr or "No Description"
        self.nav = nav
        self.actions = actions

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

    def __init__(self, obj={}):
        self.name = obj.get('name', 'n/a')
        self._obj = obj.get('object', None)


from pprint import pprint
class ConsoleView (View):
    actions ={}
    _summed_actions = {}
    _current_action = None

    def action_exit(self):
        print 'Exiting...'
        self._current_action = 'exit'

    def action_nav(self):
        nav_to = raw_input("Choose nav object\n\t: ")
        if nav_to not in self._obj.nav.keys():
            print "Wrong Object!"
        else:
            print 'nav_to ', nav_to
            print self._obj
            pprint(self._obj.nav)
            self._obj = self._obj.nav[nav_to]
            print self._obj

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
                self._summed_actions = self.actions.copy()
                self._summed_actions.update(obj.actions)
            print "Actions:"
            for n in self._summed_actions:
                print "\t",n
            action = raw_input(': ')
            if action not in self.actions.keys():
                print "Wrong Action!"
            self.actions[action]()

    def __init__(self,obj={}):
        super(ConsoleView,self).__init__(obj)
        self.actions['exit'] = self.action_exit
        self.actions['nav'] = self.action_nav


class DataField:
    pass

class URLLink:
    def __init__(self,obj={}):
        pass
        
