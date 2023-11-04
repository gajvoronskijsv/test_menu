from django.db import models


class MenuRoot(models.Model):

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    name = models.CharField('Системное название', max_length=255, blank=True, null=False)
    verbose_name = models.CharField('Отображаемое название', max_length=255, blank=True, null=False)

    def __str__(self):
        return self.verbose_name


class MenuItem(models.Model):

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'

    name = models.CharField('Название', max_length=255, blank=True, null=False)

    root = models.ForeignKey(
        MenuRoot,
        verbose_name='Родительское меню',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    path = models.CharField('Путь', max_length=1000, blank=True, null=False)

    parent = models.ForeignKey(
        'self',
        verbose_name='Родительский элемент',
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        default=0
    )

    def __str__(self):
        return self.name
