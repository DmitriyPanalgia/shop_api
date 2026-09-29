from fastapi import APIRouter, HTTPException
from app.schemas.products import Product, ProductUpdate

router = APIRouter()

products = {}
next_id = 1





@router.get("/products")
def get_products():

    return list(products.values())


@router.get("/products/{product_id}")
def get_product(product_id: int):

    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")

    return {"product_id": product_id,
            "product": products[product_id]}


@router.post("/products")
def create_product(product: Product):
    global next_id
    product_id = next_id
    products[product_id] = product
    next_id += 1

    return {"id": product_id,
            "product": product}


@router.delete("/products/{product_id}")
def delete_product(product_id: int):

    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    del products[product_id]

    return {"message": "Product deleted"}

@router.put("/products/{product_id}")
def put_product(product_id: int, product: Product):

    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    products[product_id] = product

    return {"product": product}


@router.patch("/products/{product_id}")
def patch_product(product_id: int, product: ProductUpdate):

    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")

    update_data = product.model_dump(exclude_unset=True)
    old_data = products[product_id].model_dump()

    old_data.update(update_data)

    new_product = Product(**old_data)
    products[product_id] = new_product

    return {"product": new_product}


