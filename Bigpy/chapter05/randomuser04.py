import requests


def get_random_users(count=5) : 
    url = "https://randomuser.me/api/"
    params = {"results":count}

    res=requests.get(url,params=params)
    res.raise_for_status()
    data=res.json()

    users = data['results']

    for user in users :
        first_name = user['name']['first']
        last_name = user['name']['last']
        gender = user['gender']
        country = user['location']['country']
        email =user['email']
        age = user['dob']['age']

        # print(user)
        print("이름 : ",first_name, last_name)
        print("성별 : ",gender)
        print("메일 : ",email)
        print("국가 : ",country)
        print("나이 : ",age)
        print("-"*40)


if __name__  == '__main__' :
    get_random_users()