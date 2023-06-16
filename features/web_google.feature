Feature: My fist web feature we will google for the example https://www.google.com/

  Scenario Outline: Open google page and search for panda
    When I navigate to google page
    Then I verify title on the tab will be "Google"
    When I search for "<search_item>"
    Then i validate that <search_item> will be present
    Examples:
      | search_item |
      | panda       |
      | tennis      |

