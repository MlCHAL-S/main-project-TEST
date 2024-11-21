Feature: Adding a new text

As a user,
I need to add text to db,
So that I dont forget it.

Background:
  Given the app is running
    And I navigate to the Home Page

Scenario: Add a text
  Given I enter "Some text" in the input
  When I press the "Submit" button
  Then I should see "Some text" on the web page
  Then close the browser