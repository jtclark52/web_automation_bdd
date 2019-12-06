Feature: Web UI testing using https://en.wikipedia.org.
  As a user,
  I want to be able to search using the Wikipedia website
  And be able to search for “Wake Technical Community College”

  Scenario: Basic UI serach using the Wikipedia website
    Given the url https://en.wikipedia.org
    Then I should be able to navigate to the Wikipedia Home Page
    And The Wikipedia Home page should load

  Scenario: Basic UI serach using the Wikipedia website
    Given the url https://en.wikipedia.org
    Then I should be able to search “Wake Technical Community College”
    And be able to verify that Wake Tech’s content page has a title of “Wake Technical Community College”
