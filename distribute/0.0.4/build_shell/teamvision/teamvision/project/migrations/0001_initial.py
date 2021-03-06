# Generated by Django 2.0 on 2019-02-01 07:18

from django.db import migrations, models
import model_managers.project_model_manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTaskDependency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreationTime', models.DateTimeField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('Predecessor', models.IntegerField()),
                ('Successor', models.IntegerField()),
                ('Type', models.IntegerField()),
            ],
            options={
                'db_table': 'project_task_dependency',
            },
            managers=[
                ('objects', model_managers.project_model_manager.TaskDependencyManager()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTaskOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreationTime', models.DateTimeField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('Owner', models.IntegerField()),
                ('Unit', models.FloatField(default=0)),
                ('Task', models.IntegerField()),
            ],
            options={
                'db_table': 'project_task_owner',
            },
            managers=[
                ('objects', model_managers.project_model_manager.TaskOwnerManager()),
            ],
        )


    ]
