people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):
    new_list = filter(lambda x : x != person_name, people) 

    return new_list

    
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))
