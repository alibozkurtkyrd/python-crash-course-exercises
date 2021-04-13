

def build_profile(first_name,last_name, **my_info):
    """Build my profile """

    my_profile = {}
    my_profile['first name'] = first_name
    my_profile['last name'] = last_name

    for key,value in my_info.items():
        my_profile[key] = value
    return my_profile
my_profile = build_profile('ali', 'bozkurt',
                          location = 'sivas',
                          field = 'computer science',
                          phone = '4954')
print(my_profile)
