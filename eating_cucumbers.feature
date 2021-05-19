# Created by h.ghodse at 19/05/2021
Feature: Eating Cucumbers


    Scenario: Eating all the cucumbers
        Given there are 5 cucumbers
        When I eat 3 cucumbers
        And I eat 2 cucumbers
        Then I should have 0 cucumbers
        Then all cucumbers should be accounted for

    Scenario: Eating some of the cucumbers
        Given there are 5 cucumbers
        When I eat 3 cucumbers
        Then I should have 2 cucumbers
        Then all cucumbers should be accounted for



