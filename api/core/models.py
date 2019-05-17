from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome

class Modality(models.Model):
    description = models.TextField()
    updatedOnVersion = models.BigIntegerField(editable=False)

    class Meta:
        verbose_name_plural = "Modalities"

    def __str__(self):
        return self.description

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.updatedOnVersion = DBVersion.objects.get(pk=1).version
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)


class DBVersion(models.Model):
    version = models.BigIntegerField()