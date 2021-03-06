# Generated by Django 3.2.7 on 2021-10-02 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('education', 'Education'), ('computer science', 'Computer Science'), ('mathematics', 'Mathematics'), ('engineering', 'Engineering')], default='Education', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='image_url',
            field=models.CharField(default='https://cdn-icons-png.flaticon.com/512/3135/3135773.png', max_length=200),
        ),
    ]
