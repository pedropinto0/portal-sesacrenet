# Generated by Django 3.2.7 on 2021-10-19 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_articleblogpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoBlogPage',
            fields=[
                ('blogdetailpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.blogdetailpage')),
                ('youtube_video_id', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('blog.blogdetailpage',),
        ),
    ]