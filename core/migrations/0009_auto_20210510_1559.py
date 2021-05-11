# Generated by Django 3.1.5 on 2021-05-10 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_purchaseretdtl_purchaseretmst_saleretdtl_saleretmst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedtl',
            name='mst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.purchasemst'),
        ),
        migrations.AlterField(
            model_name='purchaseretdtl',
            name='mst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.purchaseretmst'),
        ),
        migrations.AlterField(
            model_name='saleretdtl',
            name='mst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.saleretmst'),
        ),
    ]
