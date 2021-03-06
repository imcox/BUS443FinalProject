# Generated by Django 3.1.3 on 2020-11-24 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentinfo', '0006_auto_20201124_0319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.IntegerField()),
                ('major', models.CharField(max_length=500)),
                ('year', models.CharField(max_length=500)),
                ('gpa', models.DecimalField(decimal_places=1, max_digits=3)),
                ('courseid', models.IntegerField()),
                ('coursedepartment', models.CharField(max_length=500)),
                ('instructorname', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='instructorname',
        ),
    ]
