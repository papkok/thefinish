from schemas import Stubase
from pydantic import ValidationError
class Student_vald(Stubase):
 def snum1(snum:Stubase):
    a1 =0
    a2 =0
    a3 =0
    a4 =0
    resp = []
    snum1 = str(snum.STID)
    if 400 <= int(snum1[0:3]) <= 402:
        resp.append("yippee")
    else:
        resp.append("شماره سال نادرست")
        a1 = 1
    le = int(len(snum1))
    if le != 11:
        resp.append("شماره دانشجویی باید11رقم باشد.تعداد ارقام شماره دانشجویی وارد شده نادرست است")
        a2 = 1
    if int(snum1[3:9]) != 114150:
        resp.append("قسمت ثابت نادرست است.")
        a3 = 1
    if 1 <= int(snum1[9:11]) <= 99:
        resp.append("")
    else:
        resp.append("قسمت اندیس نادرست است. ")
        a4 = 1
    if a1 == 0 and a2 == 0 and a3 == 0 and a4 == 0:
        resp.append("شماره دانشجویی وارد شده درست است. شماره دانشجویی را برگرداند")
    return resp
def Fname(fname:Stubase):
    a1=0;a2=0;a3=0
    count = 0
    resp=[]
    le = int(len(fname.Fname))
    len1 = len(fname)
    if le >10:
        resp.append("نام از ده کارکتر طولانی تر است.")
        a1=1
    for i in fname.Fname:
        if i >= 'a' and i <= 'z':
            count += 1
        if i >= 'A' and i<= 'Z':
            count += 1
    if count > 0:
        resp.append("اسم خود را به فارسی وارد کنید.")
        a2=1
    if fname.isalpha() == False:
        resp.append("کارکتر های ورودی باید حروف باشند.")
        a3=1
    if a1==0 and a2==0 and a3 == 0:
        resp.append("the name is available")

    return resp
def Lname(lname:Stubase):
    a1=0;a2=0;a3=0
    count = 0
    resp=[]
    le = int(len(lname.Lname))
    len1 = len(lname.Lname)
    if le >10:
        resp.append("نام از ده کارکتر طولانی تر است.")
        a1=1
    for i in lname.Lname:
        if i >= 'a' and i <= 'z':
            count += 1
        if i >= 'A' and i<= 'Z':
            count += 1
    if count > 0:
        resp.append("اسم خود را به فارسی وارد کنید.")
        a2=1
    if (lname.Lname).isalpha() == False:
        resp.append("کارکتر های ورودی باید حروف باشند.")
        a3=1
    if a1==0 and a2==0 and a3 == 0:
        resp.append("the name is available")

    return resp
def Father_name(faname:Stubase):
    a1=0;a2=0;a3=0
    count = 0
    resp=[]
    le = int(len(faname.Father))
    len1 = len(faname.Father)
    if le >10:
        resp.append("نام از ده کارکتر طولانی تر است.")
        a1=1
    for i in faname.Father:
        if i >= 'a' and i <= 'z':
            count += 1
        if i >= 'A' and i<= 'Z':
            count += 1
    if count > 0:
        resp.append("اسم خود را به فارسی وارد کنید.")
        a2=1
    if (faname.Father).isalpha() == False:
        resp.append("کارکتر های ورودی باید حروف باشند.")
        a3=1
    if a1==0 and a2==0 and a3 == 0:
        resp.append("the name is available")

    return resp

def date_sham(inp:Stubase):
    resp= []
    if int(inp.Birth[5:7]) > 12 or int(inp.Birth[8:]) > 31:
        resp.append("قالب ورودی اشتباه.")
    else:
        resp.append("تاریخ تولد ثبت شد.")
    return resp
def passy(pasnum:Stubase):

    cou = 0
    resp = []
    p1 = pasnum.IDS[0:1]
    p2 = pasnum.IDS[1:7]
    p3 = pasnum.IDS[8:]

    if p2.isdigit() == False :
            cou += 1
    if p1==int:
        cou += 1
    if p3.isdigit() == False:
        cou += 1
    if cou != 0:
        resp.append("قالب ورودی اشتباه است.")
    return resp
def prov(prov:Stubase):
    list = ["اراک" ,'اردبیل', "تبریز", 'اصفهان' , "اهواز" , 'ایلام' , "بجنورد" , 'بندرعباس' , "بوشهر" , "بیرجند" ,
            "ارومیه" , "تهران" , "خرم آباد" , "رشت" , "زاهدان" , "زنجان" , "ساری" , "سمنان" , "سنندج","شهرکرد" ,"شیراز",
            "قزوین" "قم" , "کرج" , "کرمان" , "کرمانشاه" , "گرگان" , "مشهد" , "همدان" , "یاسوج" , "یزد", ]
    if prov.Borncity  not in list:
        return ("محل تولد باید از یکی مراکز استان باشد.")
def prov(adds:Stubase):
    le = int(len(adds.Address))
    if le > 100:
        return ("آدرس نباید بیشتر از 100 کازاکتر باشد.")
def postadd(post:Stubase):
    resp = []
    le = int(len(post.PostalCode))

    if post.PostalCode != int and le != 10:
        return 'کد پستی صحیح نمیباشد.'
    else:
        return "کد پستی صحیح میباشد"
def pnumb(numb:Stubase):
    resp= []
    le = int(len(numb.Cphone))
    if numb.Cphone[0:2] != '09' or le != 11 :
        resp.append("شماره وارد شده صحیح نمیباشید.")
    else:
        resp.append("شماره وارد شده صحیح میباشد.")

    return resp
def hnumb(numb: Stubase):
    cou = 0
    le = int(len(numb.Hphone))
    resp = []
    list1 = ["041", '044', "045", '031', "026", '084', "077", '021', "038" , "056",
             "051", "058", "061", "024", "023", "054", "071", "028", "025", "087", "034", "083",
             "074", "017", "013", "066", "011", "086", "076", "081", "035"]
    list2 = ["3", '4', '5', '8']
    if numb.Hphone[0:3] not in list1 or numb.Hphone[3] not in list2 :
        cou += 1
    if le != 11:
        cou += 1
    if cou==0:
        resp.append('شماره وارد شده صحیح است.')
    if cou !=0:
        resp.append('شماره وارد شده صحیح نیست.')
    return resp
def coll(name:Stubase):
    list= [ "فنی و مهندسی" ,'علوم پایه','علوم انسانی','دامپزشکی','اقتصاد','کشاورزی','منابع طبیعی']
    if name.Department not in list:
        return 'دانشکده غیر مجاز است.'

    else:
        return 'دانشکده انتخاب شد.'
def fos(fos:Stubase):
    foslist = ["مهندسی عمران","مهندسی مکانیک","مهندسی برق","مهندسی صنایع",
    "مهندسی شیمی","مهندسی مواد","مهندسی پزشکی","مهندسی هوافضا","مهندسی کامپیوتر","مهندسی مخازن نفت",
    "مهندسی معدن","مهندسی زلزله‌شناسی","مهندسی محیط‌زیست","مهندسی هیدرولیک","مهندسی مکاترونیک","مهندسی هسته‌ای",
    "مهندسی خودرو","مهندسی رباتیک",]
    if fos.Major  in foslist:
        return 'رشته مورد نظر انتخاب شد.'
    else:
        return 'رشته مورد نظر وجود ندارد.'
def mrstate(state:Stubase):
    list = ["مجرد" , 'متاهل']
    if state.Married in list:
        return 'وضعیت تاهل ثبت شد.'
    else:
        return 'وضعیت ورودی معتبر نیست.'
def codemel(code:Stubase):
    l = len(code.ID)
    sum = 0
    for i in range(0, l - 1):
        c = ord(code.ID[i])
        c -= 48
        sum = sum + c * (l - i)
    r = sum % 11
    c = ord(code.ID[l - 1])
    c -= 48
    if r > 2:
        r = 11 - r
    if r == c:
        return "کد ثبت شد."
    else:
        return "کد معتبر نیست."