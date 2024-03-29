# Generated by Django 2.2.3 on 2019-07-07 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_page', '0003_post_like_post_like_count_post_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='homepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorte', models.ManyToManyField(related_name='my_favor_post', to='main_page.post')),
                ('follow', models.ManyToManyField(related_name='follow_sb', to='main_page.userinfo')),
                ('my_posts', models.ManyToManyField(related_name='my_post', to='main_page.post')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_page.userinfo')),
            ],
        ),
    ]
