
def someone_profile(first,last, **user_info):
    """Build a dicitonay containing everyting we know about a userr."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

