Feature: OrangeHRM login
  Scenario: Login to hrm with valid parameters
    Given I launch chrome browser
    When i open orange HRM homepage
    And enter username "Admin" & password "admin123"
    And Click on login button
    Then User must successfully login to the dashboard page
