from behave  import given, when, then


@given('I put "{thing}" in a blenders')
def step_given_put_thing_into_blender(context, thing):
    print(f"I put {thing} in a blenders")


@when('I switch the blenders on')
def step_when_switch_blender_on(context):
    print("I switch the blenders on")


@then('it should transform intos "{other_thing}"')
def step_then_should_transform_into(context, other_thing):
    print(f"it should transform intos {other_thing}")

