# Generated by Django 3.1.3 on 2020-11-23 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentinfo', '0003_auto_20201123_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedetails',
            name='coursesectioncode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursedetails',
            name='coursetitle',
            field=models.CharField(default='course', max_length=500),
            preserve_default=False,
        ),
    ]