from behave   import given, when, then


@given('a sample text loaded into the frobulator')
def step_impl(context):
    print("Multi Line Text "+context.text)


@when('we activate the frobulator')
def step_impl(context):
    print("we activate the frobulator")


@then('we will find it similar to {language}')
def step_impl(context, language):
    print("we will find it similar to "+language)