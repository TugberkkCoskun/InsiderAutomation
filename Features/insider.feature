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
@run
Scenario: Filter the jobs by location and check related areas
    Given I am on the "Open Positions" page
    When I select the "Istanbul,Turkey" on the filter
    Then I should see the job listed appeared and contains department "QA" location "Istanbul,Turkey" and "View Now" button
    When I clicked the leftmost job
    Then I should been redirected to the lever site