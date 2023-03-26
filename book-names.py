'''
To run this program, first download books.zip from
this link: https://github.com/zygmuntz/goodbooks-10k/releases
Extract the folder and place the books.csv file
into the program's directory (CSVs of that size
will not be fully hosted by GitHub in the normal
repo).
'''

def load_all_books():
    all_books = []
    csv = open("books.csv", "r", encoding='cp850')
    for line in csv:
        cols = line.split(",")
        # 10th column is title
        all_books.append(cols[9])
    csv.close()
    return all_books

def is_taken(potential_names):
    all_books = load_all_books()
    alternate_names = get_alternate_names(potential_names)
    matches = []
    checked = 0
    
    for pn in potential_names:
        if pn in all_books:
            matches.append(pn)
        checked += 1
    for an in alternate_names:
        if an in all_books:
            matches.append(an)
        checked += 1
        if checked % 1000 == 0:
            print(f"Checked {checked} names out of {len(alternate_names)} alternate names")

    return matches

def get_alternate_names(potential_names):
    alternate_names = []
    for pn in potential_names:
        suffixes = [" of Dragons", " with Fire", " in Danger", " without Light", " of Days", " bringing Joy", " on Mars", " by the Water", " with Ire", " Shattered"]
        postsuffixes = [" Gone", " Hidden", " Lost", " Disappeared", " Running", " Hiding", " Singing", " Rising", " Falling", " Sighing"]
        postpostsuffixes = [" in Peace", " in Love", " with Ice", " out of Sight", " with no End", " Suddenly", " with Peace", " with No One", " behind the Light", " above Ground"]
        prefixes = ["In ", "On ", "With ", "Before ", "Above ", "Behind ", "Beside ", "On top of ", "By ", "Into "]
        preprefixes = ["Skeletons ", "Dragons ", "Boars ", "Witches ", "Saints ", "Soldiers ", "Warriors ", "Prisoners ", "Eagles ", "Spirits "]
        prepreprefixes = ["Black ", "White ", "Red ", "Gold ", "Metal ", "Wood ", "Pure ", "Silent ", "Grave ", "Shining "]

        for suffix in suffixes:
            for postsuffix in postsuffixes:
                for postpostsuffix in postpostsuffixes:
                    for prefix in prefixes:
                        for preprefix in preprefixes:
                            for prepreprefix in prepreprefixes:
                                alternate_names.append(prepreprefix + preprefix + prefix + pn + suffix + postsuffix + postpostsuffix)
    return alternate_names


potential_names = ['The White Crow', 'The Millenial', 'Skyscraper Plateau', 'Corporate World', 'Divergent Evolution', 'Amorphic Metal', 'Seven Worlds', 'Grenade', 'Congo', 'All Together Dead']

print("The potential names: ")
print(potential_names)
print(f"The matches: {is_taken(potential_names)}")






