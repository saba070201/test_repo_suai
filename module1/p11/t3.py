def insert_user(sourse, data, lenght):
    data.get("login", None)
    data.get("password", None)
    assert data["login"] != None and data["password"] != None
    assert len(data["password"]) < lenght
    for i in sourse:
        assert data["login"] != i["login"]
    sourse.append(data)
    return sourse


users = [
    {"login": "misha", "password": "zaq12wsx"},
    {"login": "vanya", "password": "zaq12wsx"},
    {"login": "oleg", "password": "zaq12wsx"},
]
print(insert_user(users, {"login": "Misha", "password": "zaq12wsx"}, 9))
