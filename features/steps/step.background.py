from behave  import given, when, then
import logging as logger


@given('the ninja has a {achievement_level}')
def step_the_ninja_has_a(context, achievement_level):
    print(f"the ninja has a {achievement_level}")
    logger.info("Information logged")


@when('attacked by a {opponent_role}')
def step_attacked_by_a(context, opponent_role):
    print(f"attacked by a {opponent_role}")


@when('attacked by {opponent}')
def step_attacked_by(context, opponent):
    print(f"attacked by {opponent}")


@then('the ninja should {reaction}')
def step_the_ninja_should(context, reaction):
    print(f"the ninja should {reaction}")


@given('the ninja encounters another opponent')
def step_the_ninja_encounters_another_opponent(context):
    """
    BACKGROUND steps are called at begin of each scenario before other steps.
    """
    # -- SETUP/TEARDOWN:
    print("the ninja encounters another opponent")