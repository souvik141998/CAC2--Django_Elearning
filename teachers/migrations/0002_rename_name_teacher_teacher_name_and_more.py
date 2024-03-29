# Generated by Django 5.0.1 on 2024-02-05 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='name',
            new_name='teacher_name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='email',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='file',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='image',
        ),
        migrations.AddField(
            model_name='teacher',
            name='contact_no',
            field=models.CharField(default=9964598754, max_length=15),
        ),
        migrations.AddField(
            model_name='teacher',
            name='topics_handled',
            field=models.TextField(default='maths'),
        ),
    ]
