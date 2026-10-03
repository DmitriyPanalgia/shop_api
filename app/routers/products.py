from fastapi import APIRouter, HTTPException, Depends


from app.schemas.products import Product, ProductUpdate
from sqlalchemy.orm import Session
from app.database.dependencies import get_db
from app.models.product import ProductModel


router = APIRouter()






@router.get("/products")
def get_products(db: Session = Depends(get_db)):

    returned_products = db.query(ProductModel).all()

    return returned_products


@router.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):

    returned_product = db.query(ProductModel).filter(
        ProductModel.id == product_id).first()

    if returned_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return returned_product


@router.post("/products")
def create_product(product: Product,
                   db: Session = Depends(get_db)):

    created_product = ProductModel(
        name=product.name,
        price=product.price,
        quantity=product.quantity,
    )

    db.add(created_product)
    db.commit()
    db.refresh(created_product)

    return created_product




@router.delete("/products/{product_id}")
def delete_product(product_id: int,
                   db: Session = Depends(get_db)):

    deleted_product = db.query(ProductModel).filter(
        ProductModel.id == product_id).first()

    if deleted_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(deleted_product)
    db.commit()

    return {"message": "Product deleted"}

@router.put("/products/{product_id}")
def put_product(product_id: int, product: Product,
                db: Session = Depends(get_db)):

    putted_product = db.query(ProductModel).filter(
        ProductModel.id == product_id
    ).first()

    if putted_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    putted_product.name = product.name
    putted_product.price = product.price
    putted_product.quantity = product.quantity
    db.commit()
    db.refresh(putted_product)

    return  putted_product


@router.patch("/products/{product_id}")
def patch_product(product_id: int,
                  product: ProductUpdate,
                  db: Session = Depends(get_db)):

    patched_product = db.query(ProductModel).filter(
        ProductModel.id == product_id
    ).first()

    if patched_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    update_data = product.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(patched_product, key, value)

    db.commit()
    db.refresh(patched_product)
    
    return patched_product




