Feature: INSIDER AUTOMATION TASK

Scenario: Check Career page
    Given I am on the useinsider.com website
    When I accept the cookies and  select "Career" from the Company menu in the navigation bar
    Then I should see the Career page opened and Life At Insider, Locations and Teams blocks are opened or not

Scenario: Click "See all teams" select Quality Assurance, click "See all QA jobs"
    Given I am on the "Career" page
    When I click "See all teams" button
    Then I should see the Quality Assurance job is appeared
    When I click "Quality Assurance" and I click "See all QA jobs"
    Then I should see the "Open Positions" page is opened