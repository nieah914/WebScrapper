# Generated by Django 2.1 on 2018-09-03 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='searchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testList', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='scrapper',
            name='keyword',
        ),
        migrations.AddField(
            model_name='scrapper',
            name='except_keywords',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='scrapper',
            name='optional_keywords',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='scrapper',
            name='required_keywords',
            field=models.CharField(max_length=100, null=True),
        ),
    ]