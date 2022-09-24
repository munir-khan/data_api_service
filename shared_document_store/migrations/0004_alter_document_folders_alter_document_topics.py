# Generated by Django 4.1.1 on 2022-09-24 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared_document_store', '0003_alter_document_folders_alter_document_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='folders',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared_document_store.folder'),
        ),
        migrations.AlterField(
            model_name='document',
            name='topics',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared_document_store.topic'),
        ),
    ]