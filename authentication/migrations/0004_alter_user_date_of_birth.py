# Generated by Django 5.1.2 on 2024-10-24 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
