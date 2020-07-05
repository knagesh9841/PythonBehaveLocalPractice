from behave import *


@given('we have behave installed')
def step_impl(context):
    print("we have behave installed")
    print("Browser name is "+context.browsername)


@when('we implement a test')
def step_impl(context):
    print("we implement a test")


@then('behave will test it for us!')
def step_impl(context):
    print("behave will test it for us!")

