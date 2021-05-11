# Generated by Django 3.1.5 on 2021-05-10 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210510_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasemst',
            name='customer',
        ),
        migrations.AddField(
            model_name='purchasemst',
            name='vendor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.RESTRICT, to='core.vendor'),
            preserve_default=False,
        ),
    ]