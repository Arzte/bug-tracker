# Generated by Django 3.1 on 2020-08-31 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='completed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MyUser_as_Completed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MyUser_as_Created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
