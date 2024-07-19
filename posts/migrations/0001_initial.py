# Generated by Django 5.0.7 on 2024-07-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField(blank=True, null=True)),
                ('pon_img', models.ImageField(blank=True, default='', null=True, upload_to='pons/images/%Y/%m/%d')),
                ('pon_file', models.FileField(blank=True, default='', null=True, upload_to='pons/files/%Y/%m/%d')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
