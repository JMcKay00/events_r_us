# Generated by Django 2.2.3 on 2020-03-02 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=30)),
                ('Picture', models.ImageField(blank=True, upload_to='profile_image')),
                ('password', models.CharField(blank=True, max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('EventsID', models.AutoField(primary_key=True, serialize=False)),
                ('EventName', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=500)),
                ('Picture', models.ImageField(blank=True, upload_to='')),
                ('Address', models.CharField(max_length=100)),
                ('DateTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('Rating', models.IntegerField()),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Category')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('CommentID', models.AutoField(primary_key=True, serialize=False)),
                ('Comment', models.CharField(max_length=200)),
                ('EventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Events')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.User')),
            ],
        ),
    ]