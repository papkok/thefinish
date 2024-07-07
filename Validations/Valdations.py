from re import fullmatch 
from pydantic import ValidationError
from fastapi import HTTPException
from typing import ClassVar, Dict, Any
from datetime import datetime
from . import schemas
stu = schemas.Stubase
class StudentVald(schemas.Stubase):
    resp: ClassVar[Dict[Any, Any]] = {}
    
    
    @classmethod
    def validate(cls,values: Dict[Any,Any]):
        cls.resp.clear()
        
        def snum1(snum,resp):
            snum1 = str(snum)
            if not (400 <= int(snum1[:3]) <= 402):
                resp['Student ID'] = 'شماره سال نادرست'
            if len(snum1) != 11:
                resp['Student ID'] = "شماره دانشجویی باید 11 رقم باشد."
            if snum1[3:9] != '114150':
                resp['Student ID'] = "قسمت ثابت نادرست است."
            if not (1 <= int(snum1[9:11]) <= 99):
                resp['Student ID'] = "قسمت اندیس نادرست است."
            return resp
                
                
                  

        def fname(name,resp):
            if len(name) > 10:
                resp["First Name"] = "نام از ده کارکتر طولانی تر است."
            elif any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in name):
                resp["First Name"] = "اسم خود را به فارسی وارد کنید."
            elif not name.isalpha():
                resp["First Name"] = "کارکتر های ورودی باید حروف باشند."
            return resp
                

        def lname(name,resp):
            if len(name) > 10:
                resp["Last Name"] = "نام از ده کارکتر طولانی تر است."
            elif any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in name):
                resp["Last Name"] = "نام خانوادگی خود را به فارسی وارد کنید."
            elif  name.isdigit():
                resp["Last Name"] = ".کارکتر های ورودی باید حروف باشند"
            return resp


        def father_name(name,resp):
            if len(name) > 10:
               resp["Father Name"] = "نام از ده کارکتر طولانی تر است."
            elif any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in name):
                resp["Father Name"] = "نام پدر خود را به فارسی وارد کنید."
            elif not name.isalpha():
                resp["Father Name"] = "کارکتر های ورودی باید حروف باشند."
            return resp
               

        def date_sham(date,resp):
            
            try:
                Birth = datetime.strptime(date,'%Y/%m/%d')
                if int(Birth.year) not in range(1303,1402)  or int(Birth.month) not in range(1,13) or int(Birth.day) not in range (1,32):
                   resp["Birth Date"] = "قالب ورودی اشتباه."
               
                   
            except ValueError:
                    resp["Birth Date"] = "قالب ورودی اشتباه."
            
            return resp


        def passy(id_num,resp):
            pattern = (r'^\d\d\d\d\d\d.\d\d[آ-ی]$')
            if fullmatch(pattern,id_num) == None:
                resp["Pass Number"] = ".قالب ورودی شماره شناسنامه اشتباه است."
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
                resp["Personal Phone Number"] = "شماره وارد شده صحیح نمی‌باشد."
           
            return resp    

        def hnumb(phone,resp):
            valid_area_codes = ["041", '044', "045", '031', "026", '084', "077", '021', "038", "056", "051", "058", "061",
                                "024", "023", "054", "071", "028", "025", "087", "034", "083", "074", "017", "013", "066",
                                "011", "086", "076", "081", "035"]
            if len(phone) != 11 or phone[:3] not in valid_area_codes or phone[3] not in ['3', '4', '5', '8']:
                resp['Home Phone Number'] = 'شماره وارد شده صحیح نیست.'
            return resp
                

        def coll(department,resp):
            valid_departments = ["فنی و مهندسی", 'علوم پایه', 'علوم انسانی', 'دامپزشکی', 'اقتصاد', 'کشاورزی', 'منابع طبیعی']
            if department not in valid_departments:
                resp["Department"] = 'دانشکده غیر مجاز است.'
            return resp
                

        def fos(major,resp):
            valid_majors = ["مهندسی عمران", "مهندسی مکانیک", "مهندسی برق", "مهندسی صنایع", "مهندسی شیمی", "مهندسی کامپیوتر"]
            if major not in valid_majors:
               resp["FieldofStudy"] = 'رشته تحصیلی غیر مجاز است.'
            else:
                pass
            return resp
        def mrstate(married,resp):
            list = ["مجرد" , 'متاهل']
            if married not in list:
                resp["Marrige State"] = '.وضعیت تاهل نامعتبر'
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

        
        snum1(values.get('STID'),cls.resp)
        fname(values.get('Fname'),cls.resp)
        lname(values.get('Lname'),cls.resp)
        father_name(values.get('Father'),cls.resp)
        date_sham(values.get('Birth'),cls.resp)
        passy(values.get('IDS'),cls.resp)
        prov(values.get('Borncity'),cls.resp)
        addres(values.get('Address'),cls.resp)
        postadd(values.get('PostalCode'),cls.resp)
        pnumb(values.get('Cphone'),cls.resp)
        hnumb(values.get('Hphone'),cls.resp)
        coll(values.get('Department'),cls.resp)
        fos(values.get('Major'),cls.resp)
        mrstate(values.get('Married'),cls.resp)
        codemel(values.get('ID'),cls.resp)

        
        
        return cls.resp