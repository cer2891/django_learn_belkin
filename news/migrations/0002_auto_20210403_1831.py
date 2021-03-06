# Generated by Django 3.1.7 on 2021-04-03 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='create_at',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
