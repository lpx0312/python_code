# Generated by Django 3.1.7 on 2022-03-27 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('pub_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
