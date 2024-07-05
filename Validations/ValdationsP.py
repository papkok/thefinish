from re import fullmatch 
from pydantic import ValidationError
from fastapi import HTTPException
from typing import ClassVar, Dict, Any
from datetime import datetime
from . import schemas
stu = schemas.Stubase
class ProfVald(schemas.Profbase):
    resp: ClassVar[Dict[Any, Any]] = {}
    
    
    @classmethod
    def validate(cls,values: Dict[Any,Any]):
        cls.resp.clear()

        def LID(LID,resp):
            LID1 = str(LID)
            pattern = (r'^\d\d\d\d\d\d$')
            if fullmatch(pattern,LID1) == None:
                resp["LID"] = ".کد استاد نادرست است"
        
        
        def fname(name,resp):
            if len(name) > 10:
                resp["First name"] = "نام از ده کارکتر طولانی تر است."
            elif any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in name):
                resp["First name"] = "اسم خود را به فارسی وارد کنید."
            elif  name.isdigit():
                resp["First name"] = "کارکتر های ورودی باید حروف باشند."
            return resp
                

        def lname(name,resp):
            if len(name) > 10:
                resp["Last name"] = "نام از ده کارکتر طولانی تر است."
            elif any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in name):
                resp["Last name"] = "نام خانوادگی خود را به فارسی وارد کنید."
            elif not name.isalpha():
                resp["Last name"] = ".کارکتر های ورودی باید حروف باشند"
            return resp
        

        def codemel(code,resp):
            
            l = len(code)
            sum = 0
            for i in range(0, l - 1):
                c = ord(code[i])
                c -= 48
                sum = sum + c * (l - i)
            r = sum % 11
            c = ord(code[l - 1])
            c -= 48
            if r > 2:
               r = 11 - r
            if r == c:
                pass    
            else:
                resp['ID'] = 'کد ملی معتبر نیست'
            return resp
        

        def coll(department,resp):
            valid_departments = ["فنی و مهندسی", 'علوم پایه', 'علوم انسانی', 'دامپزشکی', 'اقتصاد', 'کشاورزی', 'منابع طبیعی']
            if department not in valid_departments:
                resp["Department"] = 'دانشکده غیر مجاز است.'
            return resp
        

        def fos(major,resp):
            valid_majors = ["مهندسی عمران", "مهندسی مکانیک", "مهندسی برق", "مهندسی صنایع", "مهندسی شیمی", "مهندسی کامپیوتر"]
            if major not in valid_majors:
               resp["Field of Study"] = 'رشته تحصیلی غیر مجاز است.'
            else:
                pass
            return resp
        

        def date_sham(date,resp):
            Birth = datetime.strptime(date,'%Y/%m/%d')
            try:
                if int(Birth.year) not in range(1303,1402)  or int(Birth.month) not in range(1,13) or int(Birth.day) not in range (1,32):
                   resp["Birth Date"] = "قالب ورودی اشتباه."
               
                   
            except ValueError:
                    resp["Birth Date"] = "قالب ورودی اشتباه."
            
            return resp
        

        def prov(city,resp):
            valid_cities = ["اراک", 'اردبیل', "تبریز", 'اصفهان', "اهواز", 'ایلام', "بجنورد", 'بندرعباس', "بوشهر", "بیرجند",
                            "ارومیه", "تهران", "خرم آباد", "رشت", "زاهدان", "زنجان", "ساری", "سمنان", "سنندج", "شهرکرد", "شیراز",
                            "قزوین", "قم", "کرج", "کرمان", "کرمانشاه", "گرگان", "مشهد", "همدان", "یاسوج", "یزد"]
            if city not in valid_cities:
                resp["Born City"] = "شهر معتبر نمی‌باشد."
            else:
                pass
            return resp
        
        def addres(address,resp):
            


            if len(address) > 100:
                resp["Address"] = "آدرس ورودی از 100 کارکتر بیشتر می‌باشد."
            
            return resp    
        

        def postadd(postal_code,resp):
            postal_str = str(postal_code)
            if len(str(postal_code)) != 10 or not postal_str.isdigit():
                resp["Postal Code"] = "کد پستی صحیح نمی‌باشد."
            
            return resp    
        

        def pnumb(phone,resp):
            
            if len(phone) != 11 or not phone.startswith('09') or not phone.isdigit():
                resp["Personal Number"] = "شماره وارد شده صحیح نمی‌باشد."
           
            return resp    
   


        def hnumb(phone,resp):
            
            valid_area_codes = ["041", '044', "045", '031', "026", '084', "077", '021', "038", "056", "051", "058", "061",
                                "024", "023", "054", "071", "028", "025", "087", "034", "083", "074", "017", "013", "066",
                                "011", "086", "076", "081", "035"]
            if len(phone) != 11 or phone[:3] not in valid_area_codes or phone[3] not in ['3', '4', '5', '8']:
                resp['Home Number'] = 'شماره وارد شده صحیح نیست.'
            return resp
        

        
        LID(values.get('LID'),cls.resp)
        fname(values.get('Fname'),cls.resp)
        lname(values.get('Lname'),cls.resp)
        codemel(values.get("ID"),cls.resp)
        coll(values.get('Department'),cls.resp)
        fos(values.get('Major'),cls.resp)
        date_sham(values.get('Birth'),cls.resp)
        prov(values.get('Borncity'),cls.resp)
        addres(values.get('Address'),cls.resp)
        postadd(values.get('PostalCode'),cls.resp)
        pnumb(values.get('Cphone'),cls.resp)
        hnumb(values.get('Hphone'),cls.resp)



        return cls.resp
      