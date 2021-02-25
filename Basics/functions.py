person_list = []

def print_name(name, id = 1):
    print (name)
    person = {"name" : name, "id" : id}
    person_list.append(person)

def read_name():
    username = input("Enter username: ")
    return username
    
def list_person():
    for p in person_list:
        print(f"{p['name']} => {p['id']}")

def var_args(**args):
    print(args["name"])

#username = read_name()
#print_name(username)
#list_person()
var_args(name = "selim", age="36", worker =True)

