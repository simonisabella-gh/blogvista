# Generated by Django 4.2.16 on 2024-12-03 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_post_author_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_at',
            new_name='created_on',
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default='ben', max_length=200),
            preserve_default=False,
        ),
    ]
