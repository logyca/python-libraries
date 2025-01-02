import requests
import json
from starlette import status

def result_request(method:str,url:str,headers:dict,data:dict|str)->tuple[int,str]:
    '''Description
    :param method: method for request: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``
    :param json_data: ``json type (dict)`` or ``str``
    :return: ``http_status_code`` , ``str|error``
    '''
    try:
        if(isinstance(data,dict)):
            payload = json.dumps(data)
        else:
            payload = data

        response=requests.request(
            method.upper(),
            url,
            headers=headers,
            data=payload
        )
        return response.status_code,response.json()
    except Exception as e:
        return status.HTTP_404_NOT_FOUND,str(e)
                    
# probado en: 01. fastapi-api-key-simple  - header-list
url_api="http://127.0.0.1:8000/data/"

headers={
    "Content-Type": "application/json",
        "x-api-key": "password_key",
        "custom-header": "data-custom"
    }

json_data_dict={
    "name": "morpheus",
    "job": "leader"
}
json_data_str='''
    {
        "name": "morpheus",
        "job": "leader"
    }
'''
if __name__ == '__main__':    
    http_status_code,response=result_request('get',url_api,headers,json_data_str)
    print(json.dumps(response,indent=4))

# {
#     "api_key checked ok: ": "password_key",
#     "custom_header: ": "data-custom",
#     "headers": {
#         "host": "127.0.0.1:8000",
#         "user-agent": "python-requests/2.28.2",
#         "accept-encoding": "gzip, deflate",
#         "accept": "*/*",
#         "connection": "keep-alive",
#         "content-type": "application/json",
#         "x-api-key": "password_key",
#         "custom-header": "data-custom",
#         "content-length": "65"
#     }
# }
