# Generated by Django 4.2.1 on 2023-06-11 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nobels", "0003_alter_comment_nobel"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
