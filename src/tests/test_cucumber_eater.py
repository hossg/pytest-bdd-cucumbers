import re
from pytest_bdd import scenario, given, when, then, parsers, scenarios
from cucumber_eater import *

scenarios('.')

@given('there are <start> cucumbers', target_fixture="cucumbers")
@given(parsers.parse("there are {start:d} cucumbers"), target_fixture="cucumbers")
def start_cucumbers(start):
    assert isinstance(start,int)
    c = cucumber_eater.create_cucumber_eater(start)
    return c

@when('I eat <eat> cucumbers')
@when(parsers.parse("I eat {eat:d} cucumbers"))
def eat_cucumbers(cucumbers, eat):
    assert isinstance(eat, int)
    for i in range(eat):
        cucumber_eater.eat_cucumber(cucumbers)

@then('I should have <left> cucumbers remaining')
@then(parsers.parse("I should have {left:d} cucumbers remaining"))
def should_have_left_cucumbers(cucumbers, left):
    assert isinstance(left, int)
    assert cucumber_eater.get_cucumbers_remaining(cucumbers) == left

@then('all cucumbers should be accounted for')
def check_cucumber_count(cucumbers):
    assert cucumber_eater.check_cucumbers(cucumbers) == True
