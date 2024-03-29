# Generated by Django 2.2.7 on 2019-11-17 23:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(default='')),
                ('imag', models.ImageField(upload_to='post_img/')),
                ('created', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete='None', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
