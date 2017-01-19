from constants import Classes


def eval_obj(obj):
    'Turns dict-like description of an object into Python object'

    if 'obj' in obj[1].keys():
        obj[1]['obj'] = eval_obj(obj[1]['obj'].items()[0])
    return Classes[obj[0]](**obj[1])

def eval_recipe(recipe):
    'Setups a system with recipe'

    print recipe[1]['descr']
    result = eval_obj(recipe[1]['init'].items()[0])
    return result, result._obj