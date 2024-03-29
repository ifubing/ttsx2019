# Generated by Django 2.2.5 on 2019-09-19 12:58

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='MceTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(0, 'good'), (1, 'bad')], default=1)),
                ('detail', tinymce.models.HTMLField(verbose_name='测试富文本')),
            ],
            options={
                'verbose_name': 'test_mce',
                'verbose_name_plural': 'test_mce',
                'db_table': 'df_test_mcd',
            },
        ),
    ]
