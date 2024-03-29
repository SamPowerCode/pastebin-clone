# Generated by Django 4.1.13 on 2024-02-19 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='paste',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pastebin_app.language'),
        ),
    ]
