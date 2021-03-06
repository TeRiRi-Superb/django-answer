# Generated by Django 3.2 on 2021-12-27 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_countuser_resolution'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.CharField(max_length=20)),
                ('ask_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '高频短语',
                'verbose_name_plural': '高频短语',
                'db_table': 'chat_high',
            },
        ),
    ]
