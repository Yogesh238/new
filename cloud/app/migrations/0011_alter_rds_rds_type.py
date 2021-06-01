# Generated by Django 3.2.2 on 2021-05-24 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_project_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rds',
            name='rds_type',
            field=models.CharField(choices=[('RDS MySql', 'RDS MYSQL'), ('RDS PostGreSQl', 'RDS PostgreSQL'), ('AURORA MYSQL', 'Aurora Mysql'), ('AURORA PostGreSQL', 'Aurora PostGreSQl')], max_length=100),
        ),
    ]