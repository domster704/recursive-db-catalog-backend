from typing import Protocol


class RepositoryInterface[EntityType](Protocol):
    """Базовый интерфейс для репозиториев.

    Этот класс определяет интерфейс для работы с базой данных, включая методы для добавления,
    получения, обновления и удаления объектов.
    """

    async def add(self, entity: EntityType) -> EntityType:
        """Добавляет объект в базу данных.

        Returns:
            EntityType: Добавленный объект.
        """
        ...

    async def get(self, reference: int | str, field_search: str) -> EntityType | None:
        """Получает объект из базы данных.

        Returns:
            EntityType | None: Найденный объект или None, если объект не найден.
        """
        ...

    async def get_all(self) -> list[EntityType]:
        """Получает все объекты из базы данных.

        Returns:
            list[EntityType]: Список всех объектов.
        """
        ...

    async def get_all_by_ids(self, ids: list[int] | list[str]) -> list[EntityType]:
        """Возвращает все объекты, чьи `id` входят в переданный список.

        Returns:
            list[EntityType]: Список всех объектов.
        """
        ...

    async def delete(self, reference: int | str) -> bool:
        """Удаляет объект из базы данных.

        Returns:
            bool: True, если удаление выполнено успешно, иначе False.
        """
        ...

    async def update(self, entity: EntityType) -> EntityType:
        """Обновляет объект в базе данных.

        Returns:
            EntityType: Обновленный объект.
        """
        ...

    async def upsert(
        self,
        entity: EntityType,
        key_field: str = "id",
        commit: bool = True,
    ) -> EntityType:
        """Создаёт или обновляет объект в базе данных.

        Поведение метода:
        - Если в базе данных уже существует запись, у которой значение поля `key_field`
          совпадает со значением в переданном объекте — запись обновляется.
        - Если такой записи нет — создаётся новая.

        Args:
            entity (EntityType): Экземпляр сущности, который нужно создать или обновить.
            key_field (str, optional): Имя поля, по которому выполняется проверка существования.
                По умолчанию используется поле "id".
            commit (bool, optional): Если True — выполняется коммит после операции.

        Returns:
            EntityType: Созданная или обновлённая сущность.
        """
        ...
