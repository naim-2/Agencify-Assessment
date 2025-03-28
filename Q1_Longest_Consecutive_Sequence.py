# Takes an array of integers and returns the longest sequence of consecutive numbers in the array
def longestConsecutive(ints=[]):
    ints = sorted(list(set(x for x in ints if type(x) == int))) # checks for ints, removes duplicates and sorts the array
    if len(ints) == 0: # return empty array if empty
        return []
    
    current_ints = [] # track current array
    longest_ints = [] # track longest array

    for i in ints:
        if ints.index(i) == 0: # if first element
            current_ints.append(i) # add to current array
        if current_ints[-1] + 1 == i: # if next element is consecutive
            current_ints.append(i) # add to current array
        else: # if not consecutive
            if len(current_ints) > len(longest_ints): # if current array is longer than longest array
                longest_ints = current_ints # update longest array
            current_ints = [i] # reset current array

    return longest_ints if len(longest_ints) >= len(current_ints) else current_ints # return longest array

print(longestConsecutive([100, 4, 200, 1, 3, 2]))