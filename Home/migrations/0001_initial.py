# Generated by Django 4.0.5 on 2022-07-14 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('tag', models.CharField(max_length=100)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
