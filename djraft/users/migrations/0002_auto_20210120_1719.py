# Generated by Django 3.0.11 on 2021-01-20 10:19

from django.db import migrations, models
import djraft.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=50, unique=True, validators=[djraft.users.models.UserUsernameValidator()], verbose_name='username'),
        ),
    ]
