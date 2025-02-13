Feature: OrangeHRM Login

  Background: Comman steps
    Given I launch Browser
    When I open application
    And Enter valid username and password
    And Click on login

  Scenario: login to HRM Application
    Then User must login to the dashboard page

  Scenario: Search User
    When Navigate to search page
    Then Search page should display

  Scenario: Advance Search User
    When Navigate to Advance search page
    Then Advance Search page should display