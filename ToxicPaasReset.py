import requests,uuid,random,string
#target user send reset link
print("\n Enter the Username : ", end="")
target = input()

usr = "username"
#url/data rest instagram send link

url = "https://i.instagram.com/api/v1/accounts/send_password_reset/"            
data = {
    "_csrftoken": "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=32)),
    usr: target,
    "guid": uuid.uuid4(),
    "device_id": uuid.uuid4()
    }
headers = {"user-agent": f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; en_GB;)"}
usr = "username"

req = requests.post(url,headers=headers,data=data)
        
if "obfuscated_email" in req.text:
    print(f"[ > ] {req.text} ",end="")
    input()
    exit()
elif req.status_code == 404:
    print("Username is Not Found",end="")
    input()
    exit()
else:
    print(f"{req.text} ",end="")
    input()
    exit()
