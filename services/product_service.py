from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.product import Product
from models.category import Category
from models.supplier import Supplier

from schemas.product import (
    ProductCreate,
    ProductUpdate
)


def create_product(product: ProductCreate, db: Session):

    category = db.query(Category).filter(
        Category.id == product.category_id
    ).first()

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    supplier = db.query(Supplier).filter(
        Supplier.id == product.supplier_id
    ).first()

    if not supplier:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found"
        )

    db_product = Product(
        **product.model_dump()
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def get_all_products(db: Session):

    return db.query(Product).all()


def get_product_by_id(product_id: int, db: Session):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


def update_product(
    product_id: int,
    product_data: ProductUpdate,
    db: Session
):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    category = db.query(Category).filter(
        Category.id == product_data.category_id
    ).first()

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    supplier = db.query(Supplier).filter(
        Supplier.id == product_data.supplier_id
    ).first()

    if not supplier:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found"
        )

    for key, value in product_data.model_dump().items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    return product


def delete_product(product_id: int, db: Session):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    db.delete(product)
    db.commit()

    return {
        "message": "Product deleted successfully"
    }