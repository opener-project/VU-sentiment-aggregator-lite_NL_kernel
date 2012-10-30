Feature: Using files as input and output
  In order to tokenize text
  Using a file as an input
  Using a file as an output

  Scenario: tokenize text
    Given the fixture file "file-in-1.kaf"
    And I put it through the kernel
    Then the output should match the fixture "file-out-1.kaf"

  Scenario: tokenize negative text
    Given the fixture file "file-in-2.kaf"
    And I put it through the kernel
    Then the output should match the fixture "file-out-2.kaf"

