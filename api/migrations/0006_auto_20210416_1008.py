# Generated by Django 3.2 on 2021-04-16 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.category'),
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
    ]