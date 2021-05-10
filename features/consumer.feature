Feature: Consumer activities

    Background:
        Given User is not logged in

    Scenario: Use case required fields
        Given a web browser at Use Cases page
        When user clicks at use case page "UC1 Trespassing Monitoring & Enforcing System"
        Then informations about use case are filled:
            | informations              | filled     |
            | Use Case Number           | UC1        |
            | Use Case Domain           | Automotive |
            | Use Case Provider         | Faculty of Information Technology |

    Scenario: Only private use cases
        Given web page with all use cases private
        When user open a web browser at Use Cases page
        Then web page does not contain any use case

    Scenario: Show Methods
        Given a web browser at Home page
        When user clicks on Methods link
        Then only "Combinatorial Testing" method is visible

    Scenario: Show Tools
        Given a web browser at Home page
        When user clicks on Tools link
        Then only "Testos / Combine" method is visible