# Generated by Django 4.1.7 on 2023-02-25 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('performers', '0001_initial'),
        ('songs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('release_date', models.DateField()),
                ('performer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='performers.performer', verbose_name='Исполнитель')),
                ('record_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор записи')),
            ],
        ),
        migrations.CreateModel(
            name='AlbumSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='albums.album', verbose_name='Альбом')),
                ('record_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор записи')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='songs.song', verbose_name='Песня')),
            ],
        ),
    ]
