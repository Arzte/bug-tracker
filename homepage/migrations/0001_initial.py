# Generated by Django 3.1 on 2020-08-28 19:24

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
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('status_choices', models.CharField(choices=[('NEW', 'New'), ('IN_PROGRESS', 'In Progress'), ('DONE', 'Done'), ('INVALID', 'Invalid')], default='NEW', max_length=11)),
                ('completed_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='MyUser_as_Completed_by', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='MyUser_as_Created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]