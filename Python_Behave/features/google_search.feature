Feature: Search Feature

  Background:
    Given Navigate to google.com

  Scenario: Validate Search Feature
    When Type "selenium with python"
    And click on search button
    Then title should be selenium with python - Google Search

  Scenario: Validate Search Feature with new term
    When Type "selenium with python training"
    And click on search button
    Then title should be selenium with python - Google Search
