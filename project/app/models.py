from sqlmodel import SQLModel, Field, Relationship
from typing import List

class CategoryBase(SQLModel):
    name: str

class Category(CategoryBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    products: List["Product"] = Relationship(back_populates="category", sa_relationship_kwargs={'lazy': 'selectin'})

class CategoryRead(CategoryBase):
    id: int

class ProductBase(SQLModel):
    description: str
    price: float
    stock: int

class Product(ProductBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    category_id: int = Field(default=None, nullable=False, foreign_key='category.id')
    category: Category = Relationship(back_populates='products', sa_relationship_kwargs={'lazy': 'selectin'})

class ProductRead(ProductBase):
    id: int    

class ProductWithCategory(ProductRead):
    category: CategoryRead = None

class CategoryWithProducts(CategoryRead):
    products: List[ProductRead] = []

class UserBase(SQLModel):
    name: str
    username: str
    password: str

class User(UserBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)

class UserRead(UserBase):
    id: int

class UserCreate(UserBase):
    pass


    
