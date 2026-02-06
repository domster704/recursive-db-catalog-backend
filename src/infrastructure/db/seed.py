from datetime import date

from src.domain.entities.category import Category
from src.domain.entities.customer import Customer
from src.domain.entities.order import Order, OrderItem
from src.domain.entities.product import Product
from src.infrastructure.db.repositories.category import CategoryRepository
from src.infrastructure.db.repositories.customer import CustomerRepository
from src.infrastructure.db.repositories.order import OrderRepository
from src.infrastructure.db.repositories.order_item import OrderItemRepository
from src.infrastructure.db.repositories.product import ProductRepository
from src.infrastructure.db.uow import UnitOfWork

CATEGORY_TREE: dict[str, dict] = {
    "Бытовая техника": {
        "Стиральные машины": {
            "Фронтальные": {},
            "Вертикальные": {},
        },
        "Холодильники": {
            "Однокамерные": {},
            "Двухкамерные": {},
            "Side-by-Side": {},
        },
        "Телевизоры": {
            "LED": {},
            "OLED": {},
            "QLED": {},
        },
        "Посудомоечные машины": {},
    },
    "Компьютеры": {
        "Ноутбуки": {
            '13"': {},
            '15"': {},
            '17"': {},
        },
        "Моноблоки": {},
        "Системные блоки": {
            "Игровые": {},
            "Офисные": {},
        },
    },
    "Смартфоны и гаджеты": {
        "Смартфоны": {
            "Android": {},
            "iOS": {},
        },
        "Планшеты": {},
        "Умные часы": {},
    },
}

CUSTOMERS: list[Customer] = [
    Customer(
        name="Иван Иванов",
        address="г. Москва, ул. Пушкина, д. Колотушкина",
    ),
    Customer(
        name="Пётр Петров",
        address="г. Санкт-Петербург, Невский пр., д. 1111",
    ),
    Customer(
        name="ООО Ромашка",
        address="г. Казань, ул. Кремлёвская, д. -1",
    ),
    Customer(
        name="ООО ТехноМир",
        address="г. Екатеринбург, ул. Малышева, д. 42424242",
    ),
    Customer(
        name="АО СеверСофт",
        address="г. Новосибирск, Красный проспект, д. 01010",
    ),
    Customer(
        name="Сидоров Сергей",
        address="г. Самара, ул. Ленинградская, д. 77777",
    ),
]

PRODUCTS = [
    {
        "product": Product(
            name="Стиральная машина LG F1296HDS3 белый",
            quantity=130,
            price=37_999,
            category=None,
        ),
        "category": "Фронтальные",
    },
    {
        "product": Product(
            name="Стиральная машина Bosch WLT24460OE",
            quantity=42,
            price=49_990,
            category=None,
        ),
        "category": "Вертикальные",
    },
    {
        "product": Product(
            name="Холодильник с морозильником LG GA-B509MQSL белый",
            quantity=136,
            price=54_999,
            category=None,
        ),
        "category": "Двухкамерные",
    },
    {
        "product": Product(
            name="Холодильник Samsung RS63R5587SL",
            quantity=27,
            price=129_999,
            category=None,
        ),
        "category": "Side-by-Side",
    },
    {
        "product": Product(
            name='55" Телевизор LG OLED55C2',
            quantity=18,
            price=149_999,
            category=None,
        ),
        "category": "OLED",
    },
    {
        "product": Product(
            name='65" Телевизор Samsung QE65Q60AAU',
            quantity=31,
            price=99_999,
            category=None,
        ),
        "category": "QLED",
    },
    {
        "product": Product(
            name='17.3" Ноутбук ASUS TUF Gaming F17',
            quantity=183,
            price=83_999,
            category=None,
        ),
        "category": '17"',
    },
    {
        "product": Product(
            name='15.6" Ноутбук Apple MacBook Pro M2',
            quantity=24,
            price=214_999,
            category=None,
        ),
        "category": '15"',
    },
    {
        "product": Product(
            name="Игровой ПК Ryzen 7 / RTX 4070",
            quantity=12,
            price=189_999,
            category=None,
        ),
        "category": "Игровые",
    },
    {
        "product": Product(
            name="Офисный ПК Intel i5 / 16GB RAM",
            quantity=54,
            price=64_999,
            category=None,
        ),
        "category": "Офисные",
    },
    {
        "product": Product(
            name="Apple iPhone 15 Pro 256GB",
            quantity=76,
            price=149_999,
            category=None,
        ),
        "category": "iOS",
    },
    {
        "product": Product(
            name="Samsung Galaxy S24 Ultra",
            quantity=89,
            price=139_999,
            category=None,
        ),
        "category": "Android",
    },
]

ORDERS = [
    {
        "customer": "Иван Иванов",
        "order_date": date(2025, 12, 20),
        "status": "created",
        "items": [
            ("Стиральная машина LG F1296HDS3 белый", 1),
            ('55" Телевизор LG OLED55C2', 1),
        ],
    },
    {
        "customer": "Иван Иванов",
        "order_date": date(2026, 1, 12),
        "status": "paid",
        "items": [
            ("Samsung Galaxy S24 Ultra", 1),
        ],
    },
    {
        "customer": "Пётр Петров",
        "order_date": date(2025, 12, 22),
        "status": "paid",
        "items": [
            ("Apple iPhone 15 Pro 256GB", 2),
        ],
    },
    {
        "customer": "Пётр Петров",
        "order_date": date(2026, 2, 3),
        "status": "delivered",
        "items": [
            ('15.6" Ноутбук Apple MacBook Pro M2', 1),
        ],
    },
    {
        "customer": "ООО ТехноМир",
        "order_date": date(2026, 1, 5),
        "status": "shipped",
        "items": [
            ("Игровой ПК Ryzen 7 / RTX 4070", 1),
            ("Офисный ПК Intel i5 / 16GB RAM", 3),
        ],
    },
    {
        "customer": "ООО ТехноМир",
        "order_date": date(2026, 1, 25),
        "status": "paid",
        "items": [
            ('65" Телевизор Samsung QE65Q60AAU', 2),
            ("Samsung Galaxy S24 Ultra", 5),
        ],
    },
    {
        "customer": "АО СеверСофт",
        "order_date": date(2026, 1, 10),
        "status": "paid",
        "items": [
            ("Samsung Galaxy S24 Ultra", 10),
            ("Apple iPhone 15 Pro 256GB", 5),
        ],
    },
    {
        "customer": "АО СеверСофт",
        "order_date": date(2026, 2, 1),
        "status": "shipped",
        "items": [
            ('17.3" Ноутбук ASUS TUF Gaming F17', 10),
            ("Офисный ПК Intel i5 / 16GB RAM", 10),
        ],
    },
    {
        "customer": "ООО Ромашка",
        "order_date": date(2026, 1, 18),
        "status": "created",
        "items": [
            ("Холодильник Samsung RS63R5587SL", 1),
        ],
    },
    {
        "customer": "ООО Ромашка",
        "order_date": date(2026, 2, 5),
        "status": "cancelled",
        "items": [
            ("Стиральная машина Bosch WLT24460OE", 2),
        ],
    },
    {
        "customer": "Сидоров Сергей",
        "order_date": date(2026, 1, 30),
        "status": "paid",
        "items": [
            ("Стиральная машина Bosch WLT24460OE", 1),
            ("Холодильник с морозильником LG GA-B509MQSL белый", 1),
        ],
    },
    {
        "customer": "Сидоров Сергей",
        "order_date": date(2026, 2, 10),
        "status": "delivered",
        "items": [
            ('65" Телевизор Samsung QE65Q60AAU', 1),
        ],
    },
]


async def create_category_tree(
    repo: CategoryRepository,
    tree: dict[str, dict],
    parent: Category | None,
    cache: dict[str, Category] | None = None,
) -> None:
    if cache is None:
        cache = {}

    for name, children in tree.items():
        category = Category(
            name=name,
            parent=parent,
        )

        category = await repo.add(category)

        cache[name] = category

        await create_category_tree(
            repo=repo,
            tree=children,
            parent=category,
            cache=cache,
        )

    return cache


async def seed_initial_data():
    async with UnitOfWork() as uow:
        category_repo = CategoryRepository(uow)
        customer_repo = CustomerRepository(uow)
        product_repo = ProductRepository(uow)
        order_repo = OrderRepository(uow)
        order_item_repo = OrderItemRepository(uow)

        existing_categories = await category_repo.get_all()
        if not existing_categories:
            category_cache = await create_category_tree(
                category_repo,
                CATEGORY_TREE,
                None,
            )
        else:
            category_cache = {c.name: c for c in existing_categories}

        existing_customers = await customer_repo.get_all()
        if not existing_customers:
            for customer in CUSTOMERS:
                await customer_repo.add(customer)

        existing_products = await product_repo.get_all()
        if not existing_products:
            for item in PRODUCTS:
                product = item["product"]
                category_name = item["category"]

                product = Product(
                    name=product.name,
                    quantity=product.quantity,
                    price=product.price,
                    category=category_cache[category_name],
                )

                await product_repo.add(product)

        existing_orders = await order_repo.get_all()
        if not existing_orders:
            customers = {c.name: c for c in await customer_repo.get_all()}
            products = {p.name: p for p in await product_repo.get_all()}

            for order_data in ORDERS:
                customer = customers[order_data["customer"]]

                order = Order(
                    customer=customer,
                    order_date=order_data["order_date"],
                    status=order_data["status"],
                    items=[],
                )

                order = await order_repo.add(order)

                for product_name, quantity in order_data["items"]:
                    product = products[product_name]

                    item = OrderItem(
                        product=product,
                        quantity=quantity,
                        price=product.price,
                        order=order,
                    )

                    item = await order_item_repo.add(item, commit=False)
                    item.product = product
                    item.order = order

                    order.items.append(item)

                await uow.commit()
