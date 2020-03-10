# Generated by Django 3.0.4 on 2020-03-08 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('sales_id', models.IntegerField(primary_key=True, serialize=False)),
                ('pub_date', models.DateField(null=True)),
                ('Customer_id', models.IntegerField()),
                ('Fuel', models.CharField(max_length=50)),
                ('VEHICLE_SEGMENT', models.CharField(max_length=50)),
                ('SellingPrice', models.IntegerField(null=True)),
                ('Power_steering', models.CharField(choices=[(1, 'Yes'), (0, 'NO')], max_length=5)),
                ('airbags', models.CharField(choices=[(1, 'Yes'), (0, 'NO')], max_length=5)),
                ('sunroof', models.CharField(choices=[(1, 'Yes'), (0, 'NO')], max_length=5)),
                ('Matt_finish', models.CharField(choices=[(1, 'Yes'), (0, 'NO')], max_length=5)),
                ('music_system', models.CharField(choices=[(1, 'Yes'), (0, 'NO')], max_length=5)),
                ('Customer_Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('Customer_Incomegroup', models.CharField(max_length=200)),
                ('Customer_Region', models.CharField(max_length=200)),
                ('Customer_Marital_status', models.CharField(choices=[(1, 'Yes'), (0, 'NO')], max_length=5)),
            ],
        ),
    ]
