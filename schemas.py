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
    postalCode: int
    Cphone: int
    Hphone: int
    Department: str
    Major: str
    Married: str
    ID: int
    ScourseIDs: int
    LIDs: int


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
    LcourseID: int


class Coursbase(BaseModel):
    CID: int
    Cname: str
    Department: str
    Credit: int
    