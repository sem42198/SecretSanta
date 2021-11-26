# Generated by Django 3.2.9 on 2021-11-26 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='secret_santa.game')),
                ('secret_santa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipient', to='secret_santa.participant')),
            ],
            options={
                'unique_together': {('email', 'game')},
            },
        ),
    ]
