# Generated by Django 3.1.3 on 2020-11-23 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentinfo', '0002_coursedetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursedetails',
            name='coursesectioncode',
        ),
        migrations.RemoveField(
            model_name='coursedetails',
            name='coursetitle',
        ),
    ]
