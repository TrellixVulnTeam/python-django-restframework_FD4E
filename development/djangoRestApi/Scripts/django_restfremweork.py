import json
import os
import requests


#AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/"
AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"

REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

ENDPOINT = "http://127.0.0.1:8000/api/status/"
image_path = os.path.join(os.getcwd(), "logo.jpg")

headers = {
    "Content-type":"application/json"
    #"Authorization":"JWT" + token  #horcoded token required for testing
}

data = {
    'username':'vivek',  #vivek@gmail.cm
    'password':'vivek'
}
r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers= headers)
token = r.json()#['token']
print(token)    

# refresh_data = {
#     'token':token
# }
# new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers= headers)
# new_token = new_response.json()#['token']
# print(new_response)


# headers = {
#     #"Content-type":"application/json",
#     "Authorization":"JWT" + token
# }

# with open(image_path, 'rb') as image:
#             file_data={
#                 'image':image
#             }  
#             data= {
#                 "content":"Some random content"
#             } 
#             json_data = json.dumps(data)
#             post_data =json.dumps({"content":"Some random content"})
#             posted_response = requests.post(ENDPOINT,data=data,  headers=headers, files=file_data)
#             print(posted_response.text)

            # data= {
            #     "content":"update"
            # } 
            # json_data = json.dumps(data)
            # post_data =json.dumps({"content":"Some random content"})
            # posted_response = requests.put(ENDPOINT + str(12)+ "/",data=data,  headers=headers, files=file_data)
            # print(posted_response.text)


# headers = {
#     "Content-type":"application/json",
#     "Authorization":"JWT" + token
# }
# data= {
#     "content":"update"
# } 
# json_data = json.dumps(data)
# post_data =json.dumps({"content":"Some random content"})
# posted_response = requests.put(ENDPOINT + str(12)+ "/",data=json_data,  headers=headers)
# print(posted_response.text)

# get_endpoint = ENDPOINT + str(12)
# r = requests.get(get_endpoint)
# print(r.text)

# r2 = requests.get(ENDPOINT)
# print(r2.status_code)

# post_headers = {
#     'content-type':'application/json'
# }

# post_response = requests.post(ENDPOINT, data=post_data, headers= post_headers)
# print(post_response.text)
# def do_img(method = 'get',data={}, is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if img_path is not None:
#         with open(image_path, 'rb') as image:
#             file_data={
#                 'image':image
#             }   
#             r = requests.request(method, ENDPOINT , files=file_data, headers=headers)
#     else:
#         r = requests.request(method, ENDPOINT ,data=data, header=headers)
#     print(r.text)
#     return r 

# #do_img(method='post', data={'user':1, "content":""}, is_json= False, img_path=image_path)
# do_img(method='put', data={'id':12,'user':1, "content":""}, is_json= False, img_path=image_path)

# def do(method = 'get',data={}, id =10, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT +"?id="+str(id),data=data)
#     print(r.text)
#     return r 


# do(data={'id':500}) 
# do(method = "delete",data={'id':500})
# do(method = "put",data={'id':13, "content":"some new cool content", 'user':1})  
# do(method = "post",data={"content":"some new cool content", 'user':1})

# r = requests.request("get", "http://127.0.0.1:8000/api/status/?id=" +str(id), data={'id':12})
