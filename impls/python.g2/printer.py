import mal_types

def pr_str(obj):
    if type(obj) == list:
        s = '(' + ' '.join(pr_str(i) for i in obj) + ')'
    elif obj is None:
        s = 'nil'
    elif obj is True:
        s = 'true'
    elif obj is False:
        s = 'false'
    elif isinstance(obj, mal_types.String):
        s = f'"{obj}"'
    else:
        s = str(obj)
    return s
        
        
