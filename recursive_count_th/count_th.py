'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # Automatically checks to see if 'th' can even be in the parameter given to us
    if len(word) < 2:
        return 0


    # checks the last two portions of the string, and adds 1 to the counter and recurses & slices the last two positions
    if word[-2] == "t" and word[-1] == "h":
        return 1 + count_th(word[:-2])

    # calls the function again if the last two letters aren't 'th', and takes out the last positon for the next round through
    else:
        return count_th(word[:-1])
    
    pass
