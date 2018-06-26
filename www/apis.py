import json,logging,inspect,functools


class APIError(Exception):

    def __init__(self,error,data='',message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message



class APIValueError(APIError):
    #暗示输入值有错误或者无效，指出了输入表单的错误区域field
    def __init__(self,field,message=''):
        super(APIValueError, self).__init__('value:invalid',field,message)


class APIResourceNotFoundError(APIError):
    #暗示资源没有找到，具体指出了资源名字
    def __init__(self,field,message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound',field,message)


class APIPermissionError(APIError):
    def __init__(self,message=''):
        super(APIPermissionError, self).__init__('permission:forbidden','permission',message)