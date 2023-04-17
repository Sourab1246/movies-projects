# Generated by Django 4.2 on 2023-04-16 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='duration',
            field=models.DurationField(default='0h 0min', verbose_name='Duration'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='ratings',
            field=models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='00:00:00'),
        ),
        migrations.CreateModel(
            name='MoviesCast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appapi.cast')),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appapi.movies')),
            ],
        ),
    ]
