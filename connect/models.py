from sqlmodel import Field , SQLModel

class Survey(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    prog: str
    YL:int
    dept:str
    org:str
    achieve:str
    motto:str
    fs:str
    bmdfy:str
    ea:str



