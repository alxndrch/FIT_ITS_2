Feature: Producer activities

    Background:
        Given User is logged in as admin

    Scenario: Create valid evaluation scenario
        Given a web browser at Use Cases page
        And user clicks "Add new Evaluation Scenario"
        When "Add Evaluation Scenario" page is shown
        And user fill ES fields
            | name                                      | data      |
            | Title                                     | ES1_test  |
            | Id                                        | UC2_R_1   |
            | Evaluation Scenario Textual Description   | test      |
        Then evaluation scenario has been created
        And is private

    Scenario: Create valid use case
        Given a web browser at Use Cases page
        And user clicks on "Add new Use Case"
        When "Add Use Case" page is shown
        And user fill UC fields
            | name                  | data          |
            | Title                 | UC2_test      |
            | Use Case Number       | UC1           |
            | Use Case Domain       | Automotive    |
            | Use Case Provider     | FIT           |
            | Use Case Description  | UC2_test      |
        Then use case has been created

    Scenario: Set created use case to published
        Given a web browser at "UC2_test" page
        When state of use case is set to published by admin
        Then use case "UC2_test" is visible for not logged in user

    Scenario: Connect evaluation scenario with use case
        Given a web browser at page "Edit Use Case" of use case "UC2_test"
        When user select "Use case Evaluation Scenarios" bar
        And select evaluation scenario "ES1_test"
        Then scenario "ES1_test" is visible in "Evaluation Scenarios List" of "UC2_test"
        And is marked as private

    Scenario: Create invalid use case
        Given a web browser at Use Cases page
        And user clicks on "Add new Use Case"
        When "Add Use Case" page is shown
        And user do not fill required fields:
        Then warning is displayed

    Scenario: Create Organisation
        Given a web browser at Organisations page
        And user clicks "Add new Organisation"
        When "Add Organization" page is shown
        And user fill organisation fields:
            | name      | data      |
            | Title     | ORG1_test |
            | Acronym   | ORG       |
        Then organisation has been created

    Scenario: Only one Use Case Provider
        Given a web browser at page "Edit Use Case" of use case "UC1 Trespassing Monitoring & Enforcing System"
        
        
        When user try to add another Use Case Provider
        Then text "You can only select 1 item" is shown