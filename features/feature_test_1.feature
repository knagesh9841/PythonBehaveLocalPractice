Feature: showing off behave
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments

  Scenario: run a simple test
    Given we have behave installed
    When we implement a test
    Then behave will test it for us!