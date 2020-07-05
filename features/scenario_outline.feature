Feature: Scenario Outline (tutorial04)

  Scenario Outline: Use Blender with <thing>
    Given I put "<thing>" in a blenders
    When I switch the blenders on
    Then it should transform intos "<other thing>"

    Examples: Amphibians
        | thing         | other thing |
        | Red Tree Frog | mush        |
        | apples        | apple juice |

    Examples: Consumer Electronics
        | thing         | other thing |
        | iPhone        | toxic waste |