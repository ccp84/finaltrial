# Generated by Django 3.2.18 on 2023-04-28 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0002_alter_announcements_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcements',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='announcements',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='announcements.category'),
        ),
    ]
