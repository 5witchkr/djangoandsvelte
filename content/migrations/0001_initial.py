# Generated by Django 3.2 on 2022-03-01 04:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default=False, max_length=200)),
                ('content', models.TextField(max_length=2000)),
                ('category', models.CharField(default='All', max_length=24)),
                ('image', models.TextField(null=True)),
                ('nickname', models.CharField(default=False, max_length=24)),
                ('latitude', models.CharField(default=False, max_length=24)),
                ('longitude', models.CharField(default=False, max_length=24)),
                ('createDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]