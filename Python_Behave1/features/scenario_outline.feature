Feature: OrangeHRM login
  Scenario: Login to hrm with valid parameters
    Given I launch chrome browser
    When i open orange HRM homepage
    And enter username "Admin" & password "admin123"
    And Click on login button
    Then User must successfully login to the dashboard page

  Scenario Outline: Login to OrangeHRM with multiple parameters
    Given I launch chrome browser
    When i open orange HRM homepage
    And enter username "<username>" & password "<password>"
    And Click on login button
    Then User must successfully login to the dashboard page

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | admin    | adminxyz |