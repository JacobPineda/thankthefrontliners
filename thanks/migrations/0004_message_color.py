# Generated by Django 3.0.6 on 2020-05-25 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thanks', '0003_auto_20200524_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='color',
            field=models.CharField(choices=[('BL', 'Blue'), ('RE', 'Red'), ('YE', 'Yellow'), ('WH', 'White')], default='WH', max_length=2),
        ),
    ]
