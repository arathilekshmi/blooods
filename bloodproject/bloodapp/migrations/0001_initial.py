# Generated by Django 4.0.3 on 2022-06-06 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=6, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('age', models.CharField(blank=True, max_length=3, null=True)),
                ('address', models.TextField(blank=True, max_length=50, null=True)),
                ('blood_group', models.CharField(blank=True, choices=[('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b', 'B'), ('b-', 'B-'), ('o+', 'O+'), ('ab+', 'AB+'), ('ab-', 'AB-')], max_length=4, null=True)),
                ('center', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bloodapp.center')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bloodapp.district')),
            ],
            options={
                'db_table': 'registrations',
            },
        ),
        migrations.AddField(
            model_name='center',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloodapp.district'),
        ),
    ]
