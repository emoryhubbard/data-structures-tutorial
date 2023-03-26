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

# run it 5 times, then divide by 5 to get average
seconds = timeit.timeit("list_loops('77')", number=5, globals=globals()) / 5
ms = seconds * 1000
print(f"List_loops() average ms = {ms:.0f}")

seconds = timeit.timeit("set_loops('77')", number=5, globals=globals()) / 5
ms = seconds * 1000
print(f"Set_loops() average ms = {ms:.0f}") 

