# Generated by Django 2.2 on 2021-12-24 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_avodha_app', '0007_alter_shop_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
