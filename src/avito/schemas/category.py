from typing import Optional

from pydantic import BaseModel


class CategoryBase(BaseModel):
    id: int
    name: str
    slug: str
    description: Optional[str]


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass
