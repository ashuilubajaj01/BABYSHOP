# Generated by Django 3.0.4 on 2021-06-03 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baby', '0002_auto_20210603_0609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
