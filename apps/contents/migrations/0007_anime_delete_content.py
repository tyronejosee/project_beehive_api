# Generated by Django 5.0.1 on 2024-02-05 20:53

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0006_alter_content_episodes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(default=True, verbose_name='Available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated at')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name (ENG)')),
                ('name_jpn', models.CharField(max_length=255, unique=True, verbose_name='Name (JPN)')),
                ('image', models.ImageField(upload_to='contents/animes/', verbose_name='Image')),
                ('synopsis', models.TextField(verbose_name='Synopsis')),
                ('episodes', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1500)], verbose_name='Episodes')),
                ('duration', models.CharField(help_text='Format: "25 min. per ep."', max_length=20, verbose_name='Duration')),
                ('release', models.DateField(verbose_name='Release')),
                ('category', models.CharField(choices=[('P', 'Pending'), ('O', 'ONA'), ('S', 'Series'), ('M', 'Movies')], default='P', max_length=1, verbose_name='Category')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Airing'), ('F', 'Finished'), ('U', 'Upcoming')], default='P', max_length=1, verbose_name='Status')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.genre')),
                ('rating_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.rating')),
                ('season_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.season')),
                ('studio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.studio')),
                ('url_id', models.ManyToManyField(to='contents.url')),
            ],
            options={
                'verbose_name': 'Anime',
                'verbose_name_plural': 'Animes',
            },
        ),
        migrations.DeleteModel(
            name='Content',
        ),
    ]
