def pr_str(obj):
    if type(obj) == list:
        s = '(' + ' '.join(pr_str(i) for i in obj) + ')'
    else:
        s = str(obj)
    return s
        
        
