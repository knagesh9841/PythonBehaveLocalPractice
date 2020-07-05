from behave   import given, when, then


@given('a set of specific users')
def step_impl(context):
    for row in context.table:
        print("test data "+row["name"], ": ", row["department"])


@when('we count the number of people in each department')
def step_impl(context):
    print("we count the number of people in each department")


@then('we will find {count} people in "{department}"')
def step_impl(context, count, department):
    print(f"we will find {count} people in {department}")


@then('we will find one person in "{department}"')
def step_impl(context, department):
    print(f"we will find one person in {department}")
