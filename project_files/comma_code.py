# This is a code with a function that accept list as an argument
#  it converts the list to a string and insert the 'and' before
# last item in the list.

def comma(code=None):  # creating a function for list.

    if code is None:
        code = []
    if len(code) > 1:
        return code.insert(len(code) - 1, 'and')  # it inserted the 'and' when the parameter is passed to it.
    else:
        return code  # if the length !> 1


spam = [1, 2, 3, 4, 6]
spam2 = [str(i) for i in spam]
comma(spam2)
print(', '.join(spam2))
