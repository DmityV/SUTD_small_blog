# Generated by Django 4.2.7 on 2023-11-27 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.CharField(default='who@where.com', max_length=64, verbose_name='email'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(help_text='Укажите ФИО', max_length=128, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='to_publish',
            field=models.BooleanField(default=False, help_text='Поставьте галочку, чтобы опубликовать.', verbose_name='Проверено'),
        ),
        migrations.DeleteModel(
            name='Visitors',
        ),
    ]
