# Generated by Django 3.0.5 on 2020-06-12 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(max_length=8)),
                ('category', models.CharField(choices=[('Development', 'Development'), ('Science', 'Science'), ('Bussiness', 'Bussiness')], max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
