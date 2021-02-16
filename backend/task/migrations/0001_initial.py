# Generated by Django 3.1.5 on 2021-01-27 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('label', '0001_initial'),
        ('label', '0001_initial'),
        ('github_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='title')),
                ('description', models.CharField(max_length=1000, verbose_name='description')),
                ('due_date', models.DateTimeField(verbose_name='due date')),
                ('task_state', models.CharField(choices=[('open', 'open'), ('in progress', 'in progress'), ('closed', 'closed')], max_length=300, verbose_name='task state')),
                ('opened', models.BooleanField(default=True)),
                ('labels', models.ManyToManyField(to='label.Label')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project',
                                              verbose_name='project')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='github_user.githubuser',
                                             verbose_name='author', related_name='author')),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='github_user.githubuser',
                                               verbose_name='assignee', related_name='assignee'))
            ],
        ),
    ]
