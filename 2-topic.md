# III. Set
## Why Sets?
	Talk about applications for performance and databases.
<p>A set can get O(1) performance for finding a value. That's right, even better than O(log n). Binary search has been dethroned!</p>

## Simplest Case
<p>Put</p>
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
<p>into an arrray of 10 items.</p>
<p>If 2 goes into index 2, you can retrieve it in O(1) time.</p>
<p>But what about actual realistic numbers, that don't
	match their own index? After all, you wouldn't want to
	allocate memory for an array of billions to support an int.</p>

## Realistic numbers
<p>Put</p>
    12321, 8432, 843, 94, 5, 386, 947, 8, 99, 0
<p>into an array of 10 items.</p>
<p>If 8432 goes into index 2, you can retrieve it in O(1) time.
	How to calculate that it goes there? Use a hashing
	function to calculate the index:</p>
    hash(item) = index
<p>In its simplest form, it is just the number
	% the size of the array (if the items weren't numbers, you would need to use a proper hashing function, eg. on a string, memory address, or some kind of unique id):</p>
    8432 % 10 = 2
<p>You will immediately see a
	problem here. Where would a number like 92 go?
	Exactly over the same spot as 8432...</p>

## Conflicts
<p>You can move items over to the left or right until they find space, or you can create an array in that spot to hold multiple items. Either way, if conflicts get too frequent, your O(1) performance will be lost.</p>
<p>The key is to use a sparse list--keep the size of the array large enough so that conflicts stay infrequent, expanding as needed.</p>

## Set vs List Test Example
<p>Example problem: use Python's timing functions to benchmark performance on a certain test, for sets and for lists.</p>
    import timeit

    def list_loops(search_word):
        # build a list of "1", "2", "3", ... "100"
        words_list = []
        for i in range(100):
            words_list.append(f"{i}")

        found = 0
        for word in words_list:
            for word2 in words_list:
                for word3 in words_list:
                    if search_word in words_list:
                        found += 1
        print(found)

    def set_loops(search_word):
        # build a set of "1", "2", "3", ... "100"
        words_list = set()
        for i in range(100):
            words_list.add(f"{i}")

        found = 0
        for word in words_list:
            for word2 in words_list:
                for word3 in words_list:
                    if search_word in words_list:
                        found += 1
        print(found)

    #run it 5 times, then divide by 5 to get average
    seconds = timeit.timeit("list_loops('77')", number=5, globals=globals()) / 5
    ms = seconds * 1000
    print(f"List_loops() average ms = {ms:.0f}")

    seconds = timeit.timeit("set_loops('77')", number=5, globals=globals()) / 5
    ms = seconds * 1000
    print(f"Set_loops() average ms = {ms:.0f}")

## Book Names Problem
<p>The program starts with a list of potential books. Alternate names are created for each potential
	book, in case the first
	choice is already taken, and prints the matches that occured.<p>
<p>It checks to see if each book name is in a global list called all_books and prints the result. Afterwards, it checks to see
	if any of the alternate versions of potential names are
	taken and displays them as well.</p>
<p>The current function
	is_taken() function is mostly correct, but the all_books
	variable it references is implemented as the wrong data
	structure, causing the program to slow down too much to
	be practical. Implement the all_books and the is_taken()
	function with the right data structure.</p>
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

## Solution
    def load_all_books():
        all_books = set()
        csv = open("books.csv", "r", encoding='cp850')
        for line in csv:
            cols = line.split(",")
            all_books.add(cols[9])
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