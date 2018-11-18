# Generated by Django 2.1.1 on 2018-11-18 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('intensity', models.PositiveSmallIntegerField()),
                ('relief', models.CharField(choices=[('COMPLETE', 'Complete'), ('MODERATE', 'Moderate'), ('NONE', 'None')], max_length=20)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PrecedingSymptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trigger', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='preceding_symptoms',
            field=models.ManyToManyField(to='tracker.PrecedingSymptom'),
        ),
        migrations.AddField(
            model_name='entry',
            name='triggers',
            field=models.ManyToManyField(to='tracker.Trigger'),
        ),
        migrations.AddField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]