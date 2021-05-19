import re
from pytest_bdd import scenario, given, when, then, parsers, scenarios
import cucumber_eater

scenarios('.')
@scenario("eating_cucumbers.feature", "Eating all the cucumbers")
def test_eating_cucumbers():
    pass

@given(parsers.parse("there are {start:d} cucumbers"), target_fixture="cucumbers")
def start_cucumbers(start):
    c = cucumber_eater.create_cucumber_eater(start)
    return c

@when(parsers.parse("I eat {eat:d} cucumbers"))
def eat_cucumbers(cucumbers, eat):
    for i in range(eat):
        cucumber_eater.eat_cucumber(cucumbers)

@then(parsers.parse("I should have {left:d} cucumbers"))
def should_have_left_cucumbers(cucumbers, start, left):
    print('start {}, left {}'.format(start,left))
    assert cucumber_eater.get_cucumbers_remaining(cucumbers) == left


@then('all cucumbers should be accounted for')
def check_cucumber_count(cucumbers):
    assert cucumber_eater.check_cucumbers(cucumbers) == True
