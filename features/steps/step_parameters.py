from behave  import given, when, then


@given('I put "{thing}" in a blender')
def step_given_put_thing_into_blender(context, thing):
    print("Parameters is "+thing)
    print("Browser name is " + context.browsername)


@when('I switch the blender on')
def step_when_switch_blender_on(context):
    print("I switch the blender on")


@then('it should transform into "{other_thing}"')
def step_then_should_transform_into(context, other_thing):
    print("Another Parameter is "+other_thing)