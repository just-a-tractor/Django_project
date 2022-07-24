from django.db import models


class Organization(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return f"Название организации: {self.name}\nОписание: {self.description}"


class Shop(models.Model):
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="shops")
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    address = models.TextField("Адрес")
    index = models.IntegerField("Индекс")
    is_deleted = models.BooleanField("Удалено ли", default=False)

    def __str__(self):
        return f"Название магазина: {self.name}\nОписание: {self.description}"
