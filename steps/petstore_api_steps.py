from behave import given, when, then
from handlers.api_try import create_new_pet, get_pet_by_id, update_pet


@when(u'I add new pet to the store with status available')
def step_impl(context):
    print("test step 1 - Start***********")
    new_pet = create_new_pet()
    type_of_obj = type(new_pet)

    assert new_pet.status_code == 200
    pet_json = new_pet.json()
    context.created_pet_id = pet_json["id"]
    context.created_pet_name = pet_json["name"]
    print("test step 1 - End ***********")
    print("test step 1 - End ***********")


@then(u'Pet will be present with status "{status_text}"')
def step_impl(context, status_text):
    print("test step 2 - Start ***********")

    print(f"pet_id from context variable: {context.created_pet_id}")
    pet = get_pet_by_id(context.created_pet_id)

    assert pet.status_code == 200
    pet_json = pet.json()
    # print(pet_json)

    assert pet_json["name"] == context.created_pet_name
    assert pet_json["status"] == status_text
    # print(f"status text from feature file: {status_text}")
    print("test step 2 - End ***********")
    print("test step 2 - End ***********")


@when(u'When pet is sold it will have following data')
def step_impl(context):
    print("test step 3 - Start ***********")
    count = 1

    name = ""
    status = ""

    for row in context.table:
        print(f"Row start {count}")
        name = row["name"]
        status = row["status"]
        count += 1

    data = {
        "id": context.created_pet_id,
        "name": name,
        "status": status
    }
    print("pet - data:")
    print(data)

    response = update_pet(context.created_pet_id, name=name, status=status)
    assert response.status_code == 200
    pet_json = response.json()
    assert pet_json["name"] == name
    print(response.json())
    print("test step 3 - End ***********")
    print("test step 3 - End ***********")
    print("test step 3 - End ***********")
    print("test step 3 - End ***********")
