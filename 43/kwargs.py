def get_profile(**kwargs):
    if len(kwargs) == 0 or (len(kwargs) <= 2 and (kwargs.get('name') or kwargs.get('profession'))):
        name = kwargs.get('name', 'julian')
        profession = kwargs.get('profession', 'programmer')
        return f'{name} is a {profession}'
    else:
        raise TypeError
