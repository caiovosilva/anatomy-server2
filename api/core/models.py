from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome


class DBVersion(models.Model):
    version = models.BigIntegerField()
    clientHasDownloaded = models.BooleanField(default=False)


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


class AnatomicalRegion(models.Model):
    description = models.TextField()
    modalityFk = models.ForeignKey(Modality, on_delete=models.PROTECT)
    owner = models.ForeignKey('auth.User', related_name='anatomicalRegions', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Anatomical Regions"

    def __str__(self):
        return self.description


class Assignment(models.Model):
    description = models.TextField()
    anatomicalRegionFk = models.ForeignKey(AnatomicalRegion, on_delete=models.PROTECT)
    owner = models.ForeignKey('auth.User', related_name='assignments', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Assignments"

    def __str__(self):
        return self.description


class AnatomyImage(models.Model):
    imagePath = models.TextField()
    assignmentFk = models.ForeignKey(Assignment, on_delete=models.PROTECT)
    owner = models.ForeignKey('auth.User', related_name='anatomyImages', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Anatomy Images"

    def __str__(self):
        return self.imagePath

class Question(models.Model):
    description = models.TextField()
    assignmentFk = models.ForeignKey(Assignment, on_delete=models.PROTECT)
    owner = models.ForeignKey('auth.User', related_name='questions', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.description


class Answer(models.Model):
    description = models.TextField()
    questionFk = models.ForeignKey(Question, on_delete=models.PROTECT)
    isCorrectAnswer = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='answers', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Answers"

    def __str__(self):
        return self.description