# A sample module implementing some valuable businses fucntionality!
#
# In this case, the module simply provides some convenience functions for managing the number of cucumbers
# in a dict object, along with the number eaten, and the number remaining

def create_cucumber_eater(start):
    cucumbers = {'start': start, 'eaten': 0, 'left':start}
    return cucumbers

def eat_cucumber(cucumbers):
    if cucumbers['left'] > 0:
        cucumbers['left'] -= 1
        cucumbers['eaten'] += 1

def get_cucumbers_remaining(cucumbers):
    return cucumbers['left']

def check_cucumbers(cucumbers):
    return (cucumbers['eaten']+cucumbers['left'] == cucumbers['start'])