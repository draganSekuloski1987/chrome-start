Feature: My fist api feature we will use pet store api for this example

  Scenario: Add new pet to the store
    When I add new pet to the store with status available
    Then Pet will be present with status "available"
    When When pet is sold it will have following data
      | name  | status | id      |
      | white | sold   | unknown |




