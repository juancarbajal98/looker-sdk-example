import looker_sdk
sdk = looker_sdk.init40(config_file='./looker.ini')

my_user = sdk.me()

# output can be treated like a dictionary
print(my_user["first_name"])
# or a model instance (User in this case)
print(my_user.first_name)

# input methods can take either model instances like WriteUser
sdk.create_user(
    body=looker_sdk.models.WriteUser(first_name="Jane", last_name="Doe")
)
# or plain dictionaries
sdk.create_user(body={"first_name": "Jane", last_name: "Doe"})
print(my_user["first_name"])