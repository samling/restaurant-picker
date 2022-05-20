from typing import Union
from pydantic import BaseModel

class RestaurantBase(BaseModel):
    name:           str
    description:    Union[str, None]  = None
    food_type:      Union[str, None]  = None
    cost:           Union[int, None]  = None
    location:       Union[int, None]  = None
    has_outdoors:   Union[bool, None] = None
    bld:            Union[int, None]  = None # breakfast-lunch-dinner
    hours:          Union[str, None]  = None
    sells_alcohol:  Union[bool, None] = None

class RestaurantCreate(RestaurantBase):
    pass

class Restaurant(RestaurantBase):
    id: int
    
    class Config:
        orm_mode = True

# class User(BaseModel):
#     name: str
#     age:  int
#     veg:  bool # vegetarian

#     class Config:
#         orm_mode = True

# class UserCreate(User):
#     pass