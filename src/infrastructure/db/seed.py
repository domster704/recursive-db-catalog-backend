from src.domain.entities.category import Category
from src.domain.entities.customer import Customer
from src.domain.entities.product import Product
from src.infrastructure.db.repositories.category import CategoryRepository
from src.infrastructure.db.repositories.customer import CustomerRepository
from src.infrastructure.db.repositories.product import ProductRepository
from src.infrastructure.db.uow import UnitOfWork

CATEGORY_TREE: dict[str, dict] = {
    "Бытовая техника": {
        "Стиральные машины": {},
        "Холодильники": {
            "Однокамерные": {},
            "Двухкамерные": {},
        },
        "Телевизоры": {},
    },
    "Компьютеры": {
        "Ноутбуки": {
            '17"': {},
            '19"': {},
        },
        "Моноблоки": {},
    },
}

CUSTOMERS: list[Customer] = [
    Customer(name="Иван Иванов", address="г. Москва, ул. Пушкина, д. Колотушкина"),
    Customer(name="Пётр Петров", address="г. Санкт-Петербург, Невский пр., д. 1111"),
    Customer(name="ООО Ромашка", address="г. Казань, ул. Кремлёвская, д. -1"),
]

PRODUCTS = [
    {
        # https://www.dns-shop.ru/product/060c1f950c273332/stiralnaa-masina-lg-f1296hds3-belyj/
        "product": Product(
            name="Стиральная машина LG F1296HDS3 белый",
            quantity=130,
            price=37_999,
            category=None,
        ),
        "category": "Стиральные машины",
    },
    {
        # https://www.dns-shop.ru/product/13f1d50cf97b3330/holodilnik-s-morozilnikom-lg-ga-b509mqsl-belyj/
        "product": Product(
            name="Холодильник с морозильником LG GA-B509MQSL белый",
            quantity=136,
            price=54_999,
            category=None,
        ),
        "category": "Двухкамерные",
    },
    {
        # https://www.dns-shop.ru/product/4f2a1ba7713fed20/173-noutbuk-asus-tuf-gaming-f17-fx707zc4-hx014-seryj/
        "product": Product(
            name='17.3" Ноутбук ASUS TUF Gaming F17 FX707ZC4-HX014 серый',
            quantity=183,
            price=83_999,
            category=None,
        ),
        "category": '17"',
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
