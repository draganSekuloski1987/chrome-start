from behave import *


@when(u'I navigate to google page')
def step_impl(context):
    pass


@then(u'I verify title on the tab will be "{page_title}"')
def step_impl(context, page_title):
    print("Step 1 - Start")
    print("Page title{}".format(page_title))
    print("Step 1 - End")
    print("Step 1 - End")
    print("Step 1 - End")


@when(u'I search for "{search_item}"')
def step_impl(context, search_item):
    print("Step 2 - Start")
    print("Page title{}".format(search_item))
    print("Step 2 - End")
    print("Step 2 - End")
    print("Step 2 - End")


@then(u'i validate that "{search_item}" will be present')
def step_impl(context, search_item):
    pass
