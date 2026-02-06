from pydantic import BaseModel, Field


class CreateOrderSchema(BaseModel):
    order_id: int = Field(..., examples=[9])
    product_id: int = Field(..., examples=[32])
    quantity: int = Field(..., examples=[2])
