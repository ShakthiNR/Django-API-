# Generated by Django 4.0.6 on 2022-07-27 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreapi', '0002_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='color',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='color', to='coreapi.color'),
            preserve_default=False,
        ),
    ]