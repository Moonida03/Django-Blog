# Generated by Django 5.0.3 on 2024-05-16 18:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_post_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 16, 18, 12, 53, 496095, tzinfo=datetime.timezone.utc)),
        ),
    ]
