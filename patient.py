from pydantic import BaseModel,EmailStr,AnyUrl,Field 
from typing import List,Dict,Optional,Annotated

#THe FIELD helps us with DATA  VALIDATON,meta data ,default values


class Patient(BaseModel):
  name:Annotated[str,Field(max_length=50,title='Name of the patient',examples=['Nitish','Aryan'])]
  email:EmailStr
  url:AnyUrl
  age:int=Field(gt=0,lt=100)
  weight: float= Field(gt=0)
  married:Annotated[bool,Field(default=None,description='Is the patient married or not')]
  allergies:Optional[List[str]]
  contact_details:Dict[str,str]

def insert_patient_data(patient:Patient):

  print(patient.name)
  print(patient.age)
  print(patient.weight)
  print(patient.married)
  print(patient.allergies)

  print('inserted')

def update_patient_data(patient:Patient):

  print(patient.name)
  print(patient.age)
  print('updated')

p_info={'name':'Niyati','age':21,'weight':60,'married':False,'allergies':['cashews','dust'],'contact_details':{'phone':'9780011234','email':'abc@gmail.com'}}

p1=Patient(**p_info)

insert_patient_data(p1)