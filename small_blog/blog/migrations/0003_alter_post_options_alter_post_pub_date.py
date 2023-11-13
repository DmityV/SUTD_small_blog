# Generated by Django 4.2.7 on 2023-11-12 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_category_options_remove_category_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'default_related_name': 'posts', 'ordering': ('-pub_date',), 'verbose_name': 'публикацию', 'verbose_name_plural': 'Публикации'},
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время публикации'),
        ),
    ]
