# Generated by Django 3.0.4 on 2020-03-08 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20200309_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='Customer_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]