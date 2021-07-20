# Generated by Django 3.1.7 on 2021-05-03 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='about',
            field=models.TextField(default=0, max_length=512),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(max_length=512)),
                ('state', models.CharField(max_length=256)),
                ('district', models.CharField(max_length=256, null=True)),
                ('city', models.CharField(max_length=256, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('created', models.DateTimeField()),
                ('status', models.CharField(max_length=256)),
                ('report', models.IntegerField(default=0)),
                ('upvote', models.IntegerField(default=0)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.category')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.service')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
