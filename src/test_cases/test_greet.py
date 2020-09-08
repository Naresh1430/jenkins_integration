def greet(person):
    return "Hi {name}".format(**person)

# res = greet({"name":"Naresh"})
# print(res)

def test_greet():
    bob = {"name":"Naresh"}
    greeting= greet(bob)
    assert greeting == "Hi Naresh"