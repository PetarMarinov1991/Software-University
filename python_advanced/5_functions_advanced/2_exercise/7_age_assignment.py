def age_assignment(*args, **kwargs):
    person_info = dict()
    for name in args:
        if name[0] in kwargs:
            person_info[name] = kwargs[name[0]]
    return person_info
