from behave import fixture, use_fixture


@fixture
def selenium_browser_chrome(context):
    context.browsername = "Chrome"
    yield context.browsername
    # -- CLEANUP-FIXTURE PART:
    context.browsername = ""


def before_all(context):
    print("Before All is Called")
    use_fixture(selenium_browser_chrome, context)


def after_all(context):
    print("After All is called")


def before_step(context, step):
    print("Before Step is called")


def after_step(context, step):
    print("After Step is called")


def before_scenario(context, scenario):
    print("Before Scenario is called")


def after_scenario(context, scenario):
    print("After Scenario is called")


def before_feature(context, feature):
    print("Before feature is called")


def after_feature(context, scenario):
    print("After feature is called")

