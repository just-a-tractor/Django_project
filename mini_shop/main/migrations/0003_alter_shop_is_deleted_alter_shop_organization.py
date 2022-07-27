# Generated by Django 4.0.6 on 2022-07-25 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_shop_organization_id_alter_shop_index_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалено ли'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='main.organization'),
        ),
    ]