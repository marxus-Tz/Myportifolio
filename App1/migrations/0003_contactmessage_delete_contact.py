# Generated by Django 4.2.1 on 2023-05-23 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('hire_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]