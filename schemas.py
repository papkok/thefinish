from pydantic import BaseModel


class Stubase(BaseModel):
    STID: int
    Fname: str
    Lname: str
    Father: str
    Birth: str
    IDS: str
    Borncity: str
    Address: str
    PostalCode: int
    Cphone: str
    Hphone: str
    Department: str
    Major: str
    Married: str
    ID: str
class stuupdate(BaseModel):
    STID: int
    Fname: str
    Lname: str
    Father: str
    Birth: str
    IDS: str
    Borncity: str
    Address: str
    PostalCode: int
    Cphone: str
    Hphone: str
    Department: str
    Major: str
    Married: str
    ID: str


class Profbase(BaseModel):
    LID: int
    Fname: str
    Lname: str
    ID: int
    Department: str
    Major: str
    Birth: str
    Borncity: str
    Address: str
    PostalCode: int
    Cphone: int
    Hphone: int
    


class Coursbase(BaseModel):
    CID: int
    Cname: str
    Department: str
    Credit: int

class Courseup(BaseModel):
    CID: int
    Cname: str
    Department: str
    Credit: int
    