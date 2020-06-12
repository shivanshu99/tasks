# Generated by Django 2.2.10 on 2020-06-11 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('message', models.TextField(default='', max_length=1000)),
                ('name', models.CharField(default='', max_length=50)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('thumbnail', models.ImageField(default='', upload_to='shop/images')),
            ],
            options={
                'db_table': 'Blogpost',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('desc', models.TextField(default='', max_length=1000)),
                ('commentId', models.IntegerField(default='0')),
            ],
        ),
    ]