# Generated by Django 4.2.16 on 2024-12-10 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_rename_content_comment_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_img',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='images/'),
        ),
    ]
