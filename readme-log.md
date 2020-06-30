```console
jo@CANOAS23 MINGW64 /e/_git/model (master)
$ hp -c behave.conf --actionwords-signature
[x] Caching data: /.hiptest-publisher/cache/88ef9ab7bdcd717bf88d3c204da26028-1593535565
[v] Fetching data from HipTest
[v] Extracting data
[v] Analyzing data
[?] File /app/features/actionwords_signature.yaml exists, do you want to overwrite it? [y/N] y
[v] Exporting actionword signature: /app/features/actionwords_signature.yaml

```

```console

jo@CANOAS23 MINGW64 /e/_git/model (master)
$ hp -c behave.conf --only=features,step_definitions
[x] Caching data: /.hiptest-publisher/cache/88ef9ab7bdcd717bf88d3c204da26028-1593535650
[v] Fetching data from HipTest
[v] Extracting data
[v] Analyzing data
[v] Exporting folder "Serve coffee": /app/features/serve_coffee.feature
[v] Exporting folder "Support internationalisation": /app/features/support_internationalisation.feature
[v] Exporting folder "Can be configured": /app/features/can_be_configured.feature
[v] Exporting folder "Beans": /app/features/display_errors/beans.feature
[v] Exporting folder "Grounds": /app/features/display_errors/grounds.feature
[v] Exporting folder "Water": /app/features/display_errors/water.feature
[v] Exporting folder "Descaling": /app/features/display_errors/descaling.feature
[v] Exporting folder "Bad usage": /app/features/bad_usage.feature
[v] Exporting actionwords: ./features/steps/steps.py

jo@CANOAS23 MINGW64 /e/_git/model (master)
$ hp -c behave.conf --without=actionwords
[x] Caching data: /.hiptest-publisher/cache/88ef9ab7bdcd717bf88d3c204da26028-1593535729
[v] Fetching data from HipTest
[v] Extracting data
[v] Analyzing data
[v] Exporting folder "Serve coffee": /app/features/serve_coffee.feature
[v] Exporting folder "Support internationalisation": /app/features/support_internationalisation.feature
[v] Exporting folder "Can be configured": /app/features/can_be_configured.feature
[v] Exporting folder "Beans": /app/features/display_errors/beans.feature
[v] Exporting folder "Grounds": /app/features/display_errors/grounds.feature
[v] Exporting folder "Water": /app/features/display_errors/water.feature
[v] Exporting folder "Descaling": /app/features/display_errors/descaling.feature
[v] Exporting folder "Bad usage": /app/features/bad_usage.feature
[v] Exporting actionwords: ./features/steps/steps.py

```

```console

jo@CANOAS23 MINGW64 /e/_git/model (master)
$ behave --junit --junit-directory results
Feature: Bad usage # features/bad_usage.feature:1
  "**In order to** have coffee and let other people have to clean after me"
  "**As a** lazy coffee user"
  "**I can** ignore the message displayed by the machine"
  @priority-low
  Scenario: Full grounds does not block coffee       # features/bad_usage.feature:7
    Given the coffee machine is started              # features/steps/steps.py:42
    And I handle everything except the grounds       # features/steps/steps.py:27
    When I take "50" coffees                         # features/steps/steps.py:82
    Then message "Empty grounds" should be displayed # features/steps/steps.py:37
    And coffee should be served                      # features/steps/steps.py:67

@sprint-2
Feature: Can be configured # features/can_be_configured.feature:2
  "**In order to** get the best possible coffees"
  "**As a** geeky coffee lover"
  "**I can** configure it to match my needs"
  @priority-medium
  Scenario: Display settings            # features/can_be_configured.feature:8
    Given the coffee machine is started # features/steps/steps.py:42
    When I switch to settings mode      # features/steps/steps.py:62
    Then displayed message is           # features/steps/steps.py:77
      """
      Settings:
       - 1: water hardness
       - 2: grinder
      """

  @priority-high
  Scenario: Default settings            # features/can_be_configured.feature:19
    Given the coffee machine is started # features/steps/steps.py:42
    When I switch to settings mode      # features/steps/steps.py:62
    Then settings should be             # features/steps/steps.py:97
      | water hardness | 2      |
      | grinder        | medium |

@sprint-1
Feature: Serve coffee # features/serve_coffee.feature:2
  "**In order to** enjoy the rest of the day"
  "**As a** coffee lover"
  "**I can** get coffee from the machine"
  @priority-high
  Scenario: Simple use                  # features/serve_coffee.feature:8
    Given the coffee machine is started # features/steps/steps.py:42
    When I take a coffee                # features/steps/steps.py:107
    Then coffee should be served        # features/steps/steps.py:67

@sprint-3
Feature: Support internationalisation # features/support_internationalisation.feature:2
  "**In order to** practice my use of greetings in several languages"
  "**As a** polyglot coffee lover"
  "**I can** select the language on the coffee machine"
  @priority-medium
  Scenario Outline: Messages are based on language -- @1.1   # features/support_internationalisation.feature:14
    When I start the coffee machine using language "en"      # features/steps/steps.py:12
    Then message "Ready" should be displayed                 # features/steps/steps.py:37

  @priority-medium
  Scenario Outline: Messages are based on language -- @1.2   # features/support_internationalisation.feature:15
    When I start the coffee machine using language "fr"      # features/steps/steps.py:12
    Then message "Pret" should be displayed                  # features/steps/steps.py:37

  @priority-medium
  Scenario: No messages are displayed when machine is shut down  # features/support_internationalisation.feature:18
    Given the coffee machine is started                          # features/steps/steps.py:42
    When I shutdown the coffee machine                           # features/steps/steps.py:47
    Then message "" should be displayed                          # features/steps/steps.py:37

Feature: Beans # features/display_errors/beans.feature:1
  As a coffee lover
  I have to put fresh beans from time to time
  So I can have coffee when I need it
  Background:   # features/display_errors/beans.feature:6

  @priority-high
  Scenario: Message "Fill beans" is displayed after 38 coffees are taken  # features/display_errors/beans.feature:11
    Given the coffee machine is started                                   # features/steps/steps.py:42
    And I handle everything except the beans                              # features/steps/steps.py:32
    When I take "38" coffees                                              # features/steps/steps.py:82
    Then message "Fill beans" should be displayed                         # features/steps/steps.py:37

  @priority-low
  Scenario: It is possible to take 40 coffees before there is really no more beans  # features/display_errors/beans.feature:16
    Given the coffee machine is started                                             # features/steps/steps.py:42
    And I handle everything except the beans                                        # features/steps/steps.py:32
    When I take "40" coffees                                                        # features/steps/steps.py:82
    Then coffee should be served                                                    # features/steps/steps.py:67
    When I take a coffee                                                            # features/steps/steps.py:107
    Then coffee should not be served                                                # features/steps/steps.py:52
    And message "Fill beans" should be displayed                                    # features/steps/steps.py:37

  @priority-high
  Scenario: After adding beans, the message "Fill beans" disappears  # features/display_errors/beans.feature:24
    Given the coffee machine is started                              # features/steps/steps.py:42
    And I handle everything except the beans                         # features/steps/steps.py:32
    When I take "40" coffees                                         # features/steps/steps.py:82
    And I fill the beans tank                                        # features/steps/steps.py:92
    Then message "Ready" should be displayed                         # features/steps/steps.py:37

Feature: Descaling # features/display_errors/descaling.feature:1

  Background:   # features/display_errors/descaling.feature:4

  Scenario: Descaling is needed after 500 coffees    # features/display_errors/descaling.feature:9
    Given I handle beans                             # features/steps/steps.py:112
    And I handle water tank                          # features/steps/steps.py:102
    And I handle coffee grounds                      # features/steps/steps.py:72
    Given the coffee machine is started              # features/steps/steps.py:42
    When I take "500" coffees                        # features/steps/steps.py:82
    Then a notification about descaling is displayed # features/steps/steps.py:17
      Traceback (most recent call last):
        File "c:\python38\lib\site-packages\behave\model.py", line 1329, in run
          match.run(runner.context)
        File "c:\python38\lib\site-packages\behave\matchers.py", line 98, in run
          self.func(context, *args, **kwargs)
        File "features\steps\steps.py", line 19, in impl
          context.actionwords.a_notification_about_descaling_is_displayed()
      AttributeError: 'Actionwords' object has no attribute 'a_notification_about_descaling_is_displayed'


Feature: Grounds # features/display_errors/grounds.feature:1
  As a coffee lover
  I have to empty the grounds
  So I don't end up with a total mess around the coffee machine
  Background:   # features/display_errors/grounds.feature:6

  @priority-high
  Scenario: Message "Empty grounds" is displayed after 30 coffees are taken  # features/display_errors/grounds.feature:11
    Given the coffee machine is started                                      # features/steps/steps.py:42
    And I handle everything except the grounds                               # features/steps/steps.py:27
    When I take "30" coffees                                                 # features/steps/steps.py:82
    Then message "Empty grounds" should be displayed                         # features/steps/steps.py:37

  @priority-medium
  Scenario: When the grounds are emptied, message is removed  # features/display_errors/grounds.feature:16
    Given the coffee machine is started                       # features/steps/steps.py:42
    And I handle everything except the grounds                # features/steps/steps.py:27
    When I take "30" coffees                                  # features/steps/steps.py:82
    And I empty the coffee grounds                            # features/steps/steps.py:57
    Then message "Ready" should be displayed                  # features/steps/steps.py:37

Feature: Water # features/display_errors/water.feature:1
  As a coffee lover
  I have to handle the water tank
  So I can have coffee when I need it
  Background:   # features/display_errors/water.feature:6

  @priority-high
  Scenario: Message "Fill water tank" is displayed after 50 coffees are taken  # features/display_errors/water.feature:11
    Given the coffee machine is started                                        # features/steps/steps.py:42
    And I handle everything except the water tank                              # features/steps/steps.py:22
    When I take "50" coffees                                                   # features/steps/steps.py:82
    Then message "Fill tank" should be displayed                               # features/steps/steps.py:37

  @priority-low
  Scenario: It is possible to take 10 coffees after the message "Fill water tank" is displayed  # features/display_errors/water.feature:16
    Given the coffee machine is started                                                         # features/steps/steps.py:42
    And I handle everything except the water tank                                               # features/steps/steps.py:22
    When I take "60" coffees                                                                    # features/steps/steps.py:82
    Then coffee should be served                                                                # features/steps/steps.py:67
    When I take a coffee                                                                        # features/steps/steps.py:107
    Then coffee should not be served                                                            # features/steps/steps.py:52

  @priority-high
  Scenario: When the water tank is filled, the message disappears  # features/display_errors/water.feature:23
    Given the coffee machine is started                            # features/steps/steps.py:42
    And I handle everything except the water tank                  # features/steps/steps.py:22
    When I take "55" coffees                                       # features/steps/steps.py:82
    And I fill the water tank                                      # features/steps/steps.py:87
    Then message "Ready" should be displayed                       # features/steps/steps.py:37


Failing scenarios:
  features/display_errors/descaling.feature:9  Descaling is needed after 500 coffees

7 features passed, 1 failed, 0 skipped
15 scenarios passed, 1 failed, 0 skipped
66 steps passed, 1 failed, 0 skipped, 0 undefined
Took 0m0.028s
```