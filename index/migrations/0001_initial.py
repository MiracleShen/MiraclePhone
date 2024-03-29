# Generated by Django 3.2.6 on 2021-09-04 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Catagory', models.CharField(max_length=60, verbose_name='类别')),
                ('Title', models.CharField(max_length=20, verbose_name='标题')),
                ('Content', models.CharField(max_length=11, null=True, verbose_name='内容')),
                ('createdtime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updatedtime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name_plural': '新闻',
            },
        ),
    ]
