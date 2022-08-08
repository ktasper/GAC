"""
This module preforms all the data manipulation
"""



def user_dict_to_json(users_dict):
    """
    This takes in a users dict and returns a json object
    """
    new_user_perms = {}
    for user in users_dict:
        user_perms = users_dict[user].permissions
        user_perms = str(user_perms)
        # Gets a list of all the users permissions
        list_of_user_perms = user_perms.split('(')[1].strip(')(').split(',')
        # Remove all the permissions with the word "False"
        removed_false = [ x for x in list_of_user_perms if "False" not in x ]
        # Now we can remove the "=True" since all the remaining permissions are True
        for remaining in removed_false:
            new_user_perms[user] = remaining.split("=")[0].strip(' ')
    print (new_user_perms)
