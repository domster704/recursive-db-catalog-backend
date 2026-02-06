from src.application.exceptions.not_enough_product import NotEnoughProductQuantity
from src.application.exceptions.not_found import NotFound
from src.domain.entities.order import Order, OrderItem
from src.domain.entities.product import Product
from src.domain.repositories.base import RepositoryInterface


class CreateOrderUseCase(object):
    def __init__(
        self,
        order_repository: RepositoryInterface[Order],
        order_item_repository: RepositoryInterface[OrderItem],
        product_repository: RepositoryInterface[Product],
    ):
        self.order_repository = order_repository
        self.order_item_repository = order_item_repository
        self.product_repository = product_repository

    async def execute(self, order_id: int, product_id: int, quantity: int) -> None:
        order: Order | None = await self.order_repository.get(
            order_id, field_search="id"
        )
        product: Product | None = await self.product_repository.get(
            product_id, field_search="id"
        )

        if order is None or product is None:
            raise NotFound("Order или Product не найдены")

        if product.quantity < quantity:
            raise NotEnoughProductQuantity(
                f"Доступно {product.quantity}, запрошено {quantity}"
            )

        find: bool = False
        for item in order.items:
            if item.product.id == product.id:
                new_quantity = item.quantity + quantity
                if product.quantity < new_quantity:
                    raise NotEnoughProductQuantity(
                        f"Доступно {product.quantity}, запрошено {new_quantity}"
                    )

                item.quantity = new_quantity
                item.price = product.price * new_quantity
                await self.order_item_repository.update(item)
                return None

        order_item = OrderItem(
            product=product,
            quantity=quantity,
            price=product.price * quantity,
            order=order,
        )
        await self.order_item_repository.add(order_item)
        return None
