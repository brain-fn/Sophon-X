
IModeRecipe = {
    'IMode' : {
        'descr': "IMode: just make a RootInterface and connect to it ConsoleView",
        'plugins': 'all',
        'init':{
            'core.ConsoleView': {
                'name'  : "Root View",
                'descr' : "Interactive console session",
                'obj': {
                    'core.Interface': {
                        'name':'Root Interface',
                        'descr':'Root Interface'}},
                }
        }
    }}
