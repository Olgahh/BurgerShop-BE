# Generated by Django 3.0.5 on 2020-04-09 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Food',
            },
        ),
    ]
