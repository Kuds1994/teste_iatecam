from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List

from app.db import get_session
from app.models import Product, User, Category, ProductWithCategory, UserRead, UserCreate

app = FastAPI()


@app.get("/products", response_model=List[ProductWithCategory])
async def get_products(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Product))
    products = result.scalars().all()
    if not products:
        raise HTTPException(status_code=404, detail="Nenhum produto encontrado")
    return products
    ##return [Product(id=product.id, description=product.description, price=product.price, stock=product.stock, category=category) for product, category in products]


@app.post("/product")
async def add_song(product: Product, session: AsyncSession = Depends(get_session)):
    product = Product(description=product.description, price=product.price, stock=product.stock, category_id=product.category_id)
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product

@app.post("/user", response_model=UserRead)
async def add_song(user: UserCreate, session: AsyncSession = Depends(get_session)):
    user = User.from_orm(user)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user