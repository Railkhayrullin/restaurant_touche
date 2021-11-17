from django.db import models


class ContactInfo(models.Model):
    """Контактная информация"""
    class Meta:
        verbose_name = "контактная информация"
        verbose_name_plural = "контактная информация"

    city_postcode = models.CharField("город и почтовый индекс", max_length=128, default='')
    street_building = models.CharField("улица и номер здания", max_length=128, default='')
    from_hour_mon_thurs = models.TimeField("время открытия Пн-Чт", default='10:00:00')
    to_hour_mon_thurs = models.TimeField("время закрытия Пн-Чт", default='23:00:00')
    from_hour_fri_sun = models.TimeField("время открытия Пт-Вс", default='11:00:00')
    to_hour_fri_sun = models.TimeField("время закрытия Пт-Вс", default='02:00:00')
    contact_phone = models.CharField("контактный номер", max_length=16)
    reservation_phone = models.CharField("номер для бронирования столиков", max_length=16)
    email = models.EmailField("email", max_length=128)

    def __str__(self):
        return self.city_postcode
