@feature_type_1 @my_custom_tag
Feature: Tinkoff Mobile answering machine
# created by admin | last edited by admin, 09-01-2021 09:00:00 | published by admin
Tasks: PRJ-1234, PRJ-1235

Background:
  Given application TINKOFF_MOBILE
  And call from +79123456789 to +79123456790

Scenario: The bot answers the caller as an answering machine
  When got through
  Then bot says "The subscriber cannot answer. I am an assistant Oleg, what should I convey? I will write down"

  When I say "Yes. Tell me that your master owes me."
  Then bot says "Ok I'll pass it on. Anything else?"

  When I hang up
  Then call ends
