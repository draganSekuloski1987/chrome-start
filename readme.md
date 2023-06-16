## Python trial project

# pycharm format shortcut press " ⌘ ⌥ L "

# Create project in pycharm - create new project

1. Add project name
2. In the new env using choose “Virtualenvironment” from the dropdown
3. Press on create button - > Project will be created

# Install packages in the vev in the project

1. chek python version “ $ python —version” or “ python3 —version” -> Should return current python version
2. check installed packages “$ pip freeze” -> no packages will be installed
3. Install requests “ $ python3 -m pip install requests “
4. Install selenium “ $ python3 -m pip install selenium “
5. Install webdriver-manager “ $ python3 -m pip install webdriver-manager “
6. Install behave “ $ python3 -m pip install behave “
7. Install allure-behave for reports “ $ python3 -m pip install allure-behave
8. Install pytest for reports “ $ python3 -m pip install pytest”
9. check installed packages “$ pip freeze” -> all packages should have been present
10. Create requirements file “ $ pip freeze > requirements.txt”
11. To install everything from the requirements.txt “ $ python3 -m pip install -r requirements.txt”

# Activate virtual env in case is not activated

1. Run the following “$ source venv/bin/activate”

# Create a project structure

1. create “.gitignore” file and add virtual environment inside “venv/“
2. Create environment.py file for build and tear down steps
3. Create features package and create a feature files petstore_api and web.feature
4. Create steps package and create a feature files petstore_api_steps.py and web_steps.py
5. Create handlers package

# API feature

1. Inside petstore_api.feature file create Feature, Scenario and steps for the scenario
2. Run command in terminal “$ behave --dry-run --no-capture --format=steps features/petstore_api.feature” -> To generate
   steps
3. Copy the steps and add them into the petstore_api_steps.py
4. In the top of the import “from behave import given, when, then”
5. Add print statements inside the steps and run the behave feature “behave features/petstore_api.feature”
6. In order to see the print statement run the test as “$ behave features/petstore_api.feature --no-capture --format
   plain”

# Pasing the context from one step to another

1. It can be done via context.<variable name> = <value>


# Web feature
1. Inside web_google.feature file create Feature, Scenario and steps for the scenario
2. Run command in terminal “$ behave --dry-run --no-capture --format=steps features/web_google.feature” -> To generate
   steps
