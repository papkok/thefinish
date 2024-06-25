from re import fullmatch 
from . import schemas
from pydantic import ValidationError
from fastapi import HTTPException
from typing import ClassVar, Dict, Any
from datetime import datetime

class StudentVald(schemas.Stubase):
    resp: ClassVar[Dict[Any, Any]] = {}
    

    @classmethod
    def validate(cls, values: Dict[Any,Any]):
        cls.resp.clear()
        
        def snum1(snum):
            snum1 = str(snum)
            if not (400 <= int(snum1[:3]) <= 402):
                cls.resp['snum.STID'] = 'شماره سال نادرست'
            if len(snum1) != 11:
                cls.resp['snum.STID'] = "شماره دانشجویی باید 11 رقم باشد."
            if snum1[3:9] != '114150':
                cls.resp['snum.STID'] = "قسمت ثابت نادرست است."
            if not (1 <= int(snum1[9:11]) <= 99):
                cls.resp['snum.STID'] = "قسمت اندیس نادرست است."
            if 'snum.STID' not in cls.resp:
                cls.resp["snum.STID"] = "شماره دانشجویی وارد شده درست است."

        def fname(name):
            if len(name) > 10:
                cls.resp["fname.Fname"] = "نام از ده کارکتر طولانی تر است."
            elif any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in name):
                cls.resp["fname.Fname"] = "اسم خود را به فارسی وارد کنید."
            elif not name.isalpha():
                cls.resp["fname.Fname"] = "کارکتر های ورودی باید حروف باشند."
            else:
                cls.resp["fname.Fname"] = ".نام شما معتبر است "

        def lname(name):
            if len(name) > 10:
                cls.resp["lname.Lname"] = "نام از ده کارکتر طولانی تر است."
            elif any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in name):
                cls.resp["lname.Lname"] = "نام خانوادگی خود را به فارسی وارد کنید."
            elif not name.isalpha():
                cls.resp["lname.Lname"] = ".کارکتر های ورودی باید حروف باشند"
            else:
                cls.resp["lname.Lname"] = " .نام خانوادگی شما معتبر است"

        def father_name(name):
            if len(name) > 10:
                cls.resp["father_name.Father"] = "نام از ده کارکتر طولانی تر است."
            elif any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in name):
                cls.resp["father_name.Father"] = "نام پدر خود را به فارسی وارد کنید."
            elif not name.isalpha():
                cls.resp["father_name.Father"] = "کارکتر های ورودی باید حروف باشند."
            else:
                cls.resp["father_name.Father"] = "نام پدر شما معتبر است."

        def date_sham(date):
            Birth = datetime.strptime(date,'%Y/%m/%d')
            try:
                if int(Birth.year) not in range(1303,1402)  or int(Birth.month) not in range(1,13) or int(Birth.day) not in range (1,32):
                   cls.resp["date_sham.Birth"] = "قالب ورودی اشتباه."
                else:
                   cls.resp["date_sham.Birth"] = "تاریخ تولد ثبت شد."
            except ValueError:
                    cls.resp["date_sham.Birth"] = "قالب ورودی اشتباه."
            



        def passy(id_num):
            pattern = (r'^\d\d\d\d\d\d.\d\d[آ-ی]$')
            if fullmatch(pattern,id_num) == None:
                cls.resp["passy.IDS"] = ".قالب ورودی شماره شناسنامه اشتباه است."
            else:
                cls.resp["passy.IDS"] = ".شماره شناسنامه معتبر است."

        def prov(city):
            valid_cities = ["اراک", 'اردبیل', "تبریز", 'اصفهان', "اهواز", 'ایلام', "بجنورد", 'بندرعباس', "بوشهر", "بیرجند",
                            "ارومیه", "تهران", "خرم آباد", "رشت", "زاهدان", "زنجان", "ساری", "سمنان", "سنندج", "شهرکرد", "شیراز",
                            "قزوین", "قم", "کرج", "کرمان", "کرمانشاه", "گرگان", "مشهد", "همدان", "یاسوج", "یزد"]
            if city not in valid_cities:
                cls.resp["prov.Borncity"] = "شهر معتبر نمی‌باشد."
            else:
                cls.resp["prov.Borncity"] = "شهر معتبر است."

        def addres(address):
            if len(address) > 100:
                cls.resp["addres.Address"] = "آدرس ورودی از 100 کارکتر بیشتر می‌باشد."
            else:
                cls.resp["addres.Address"] = "آدرس شما ثبت شد."

        def postadd(postal_code):
            postal_str = str(postal_code)
            if len(str(postal_code)) != 10 or not postal_str.isdigit():
                cls.resp["postadd.PostalCode"] = "کد پستی صحیح نمی‌باشد."
            else:
                cls.resp["postadd.PostalCode"] = "کد پستی صحیح می‌باشد."


        def pnumb(phone):
            
            if len(str(phone)) != 11 or not phone.startswith('09') or not phone.isdigit():
                cls.resp["pnumb.Cphone"] = "شماره وارد شده صحیح نمی‌باشد."
            else:
                cls.resp["pnumb.Cphone"] = "شماره وارد شده صحیح می‌باشد."

        def hnumb(phone):
            valid_area_codes = ["041", '044', "045", '031', "026", '084', "077", '021', "038", "056", "051", "058", "061",
                                "024", "023", "054", "071", "028", "025", "087", "034", "083", "074", "017", "013", "066",
                                "011", "086", "076", "081", "035"]
            if len(str(phone)) != 11 or phone[:3] not in valid_area_codes or phone[3] not in ['3', '4', '5', '8']:
                cls.resp['hnumb.Hphone'] = 'شماره وارد شده صحیح نیست.'
            else:
                cls.resp['hnumb.Hphone'] = 'شماره وارد شده صحیح است.'

        def coll(department):
            valid_departments = ["فنی و مهندسی", 'علوم پایه', 'علوم انسانی', 'دامپزشکی', 'اقتصاد', 'کشاورزی', 'منابع طبیعی']
            if department not in valid_departments:
                cls.resp["coll.Department"] = 'دانشکده غیر مجاز است.'
            else:
                cls.resp['coll.Department'] = 'دانشکده انتخاب شد.'

        def fos(major):
            valid_majors = ["مهندسی عمران", "مهندسی مکانیک", "مهندسی برق", "مهندسی صنایع", "مهندسی شیمی", "مهندسی کامپیوتر"]
            if major not in valid_majors:
                cls.resp["fos.FieldofStudy"] = 'رشته تحصیلی غیر مجاز است.'
            else:
                cls.resp['fos.FieldofStudy'] = 'رشته تحصیلی انتخاب شد.'

        try:
            snum1(values.get('STID', ''))
            fname(values.get('Fname', ''))
            lname(values.get('Lname', ''))
            father_name(values.get('Father', ''))
            date_sham(values.get('Birth', ''))
            passy(values.get('IDS', ''))
            prov(values.get('Borncity', ''))
            addres(values.get('Address', ''))
            postadd(values.get('PostalCode', ''))
            pnumb(values.get('Cphone', ''))
            hnumb(values.get('Hphone', ''))
            coll(values.get('Department', ''))
            fos(values.get('FieldofStudy', ''))
        except KeyError as ke:
            raise HTTPException(status_code=400, detail=f'Missing {ke!r}')
        except ValidationError as ve:
            raise HTTPException(status_code=422, detail=f'Validation error: {ve}')
        
        return values