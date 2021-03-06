# Generated by Django 4.0.4 on 2022-05-06 12:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_employee_dept'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageTest',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
