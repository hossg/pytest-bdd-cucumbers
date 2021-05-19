
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