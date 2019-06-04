# Generated by Django 2.0.13 on 2019-05-27 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_dbversion'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnatomicalRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Anatomical Regions',
            },
        ),
        migrations.CreateModel(
            name='AnatomyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagePath', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Anatomy Images',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('isCorrectAnswer', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Answers',
            },
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('anatomicalRegionFk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.AnatomicalRegion')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Assignments',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('assignmentFk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Assignment')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.AddField(
            model_name='dbversion',
            name='clientHasDownloaded',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='modality',
            name='updatedOnVersion',
            field=models.BigIntegerField(editable=False),
        ),
        migrations.AddField(
            model_name='answer',
            name='questionFk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Question'),
        ),
        migrations.AddField(
            model_name='anatomyimage',
            name='assignmentFk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Assignment'),
        ),
        migrations.AddField(
            model_name='anatomyimage',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anatomyImages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='anatomicalregion',
            name='modalityFk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Modality'),
        ),
        migrations.AddField(
            model_name='anatomicalregion',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anatomicalRegions', to=settings.AUTH_USER_MODEL),
        ),
    ]