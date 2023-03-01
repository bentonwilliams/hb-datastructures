"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    

    species = set()


    # TODO: replace this with your code
    with open(filename) as villagers:
        for villager in villagers:
            species.add(villager.split("|")[1])
    
    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []
    with open(filename) as all_villagers:
        for villager in all_villagers:
            name=villager.split("|")[0]
            species=villager.split("|")[1]
            if search_string=="All":
                villagers.append(name)
            else:
                if search_string==species:
                    villagers.append(name)

    # TODO: replace this with your code

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code
    hobbies=set()
    grouped_villagers=[]
    all_villagers=all_data(filename)
    for line in all_villagers:
        hobbies.add(line[3])
    print(hobbies)
    for hobby in hobbies:
        villagers_with_common_hobby=[]
        for line in all_villagers:
            if line[3]==hobby:
                print('this got triggered')
                villagers_with_common_hobby.append(line[0])
        grouped_villagers.append(villagers_with_common_hobby) 

        

    return grouped_villagers


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []
    with open(filename) as f:
        for line in f:
            name,species,personality,hobby,motto=line.split("|")
            all_data.append((name,species,personality,hobby,motto))
    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code
    all_villagers=all_data(filename)
    for villager in all_villagers:
        if villager[0]==villager_name:
            return villager[4]
    return None

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
    likeminded_villagers=set()
    all_villagers=all_data(filename)
    for villager in all_villagers:
        if villager[0]==villager_name:
            search_personality=villager[2]
            break
    for villager in all_villagers:
        if villager[2]==search_personality:
            likeminded_villagers.add(villager[0])
    return likeminded_villagers


# testing:
# filename='villagers.csv'
# print(all_species(filename))
# print(get_villagers_by_species(filename))
# print(all_names_by_hobby(filename))
# print(find_likeminded_villagers(filename,"Wendy"))

