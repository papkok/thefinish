from re import fullmatch 
from pydantic import ValidationError
from fastapi import HTTPException
from typing import ClassVar, Dict, Any
from datetime import datetime
from . import schemas
stu = schemas.Stubase
class CousVald(schemas.Coursbase):
    resp: ClassVar[Dict[Any, Any]] = {}
    
    
    @classmethod
    def validate(cls,values: Dict[Any,Any]):
        cls.resp.clear()
    
        def CID(CID,resp):
            CID1 = str(CID)
            pattern = (r'^\d\d\d\d\d$')
            if fullmatch(pattern,CID1) == None:
                resp["CID"] = ".کد درس اشتباه است"
            return resp
            
            
     
    
        def fname(name,resp):
            
            if len(name) > 25:
                resp["Course name"] = "نام درس از 25 کارکتر طولانی تر است."
            elif any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in name):
                resp["Course name"] = "اسم درس را به فارسی وارد کنید."
            elif  name.isdigit():
                resp["Course name"] = "کارکتر های ورودی باید حروف باشند."
            return resp
    
    
        def coll(department,resp):
            valid_departments = ["فنی و مهندسی", 'علوم پایه', 'علوم انسانی', 'دامپزشکی', 'اقتصاد', 'کشاورزی', 'منابع طبیعی']
            if department not in valid_departments:
                resp["Department"] = 'دانشکده غیر مجاز است.'
            return resp
    
        def Credit(crd,resp):
            crd1 = str(crd)
            pattern = (r'[1-4]')
            if fullmatch(pattern,crd1) == None:
               resp["Credit"] = ".تعداد واحد غیر مجاز است"

        CID(values.get('CID'),cls.resp)
        fname(values.get('Cname'),cls.resp)
        coll(values.get("Department"),cls.resp)
        Credit(values.get("Credit"),cls.resp)


        return cls.resp