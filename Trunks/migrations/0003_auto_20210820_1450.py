# Generated by Django 2.2.24 on 2021-08-20 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Trunks', '0002_auto_20210820_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTN_Trunk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trunk', models.CharField(max_length=20)),
                ('Detail', models.TextField()),
                ('Created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Published_date', models.DateTimeField(blank=True, null=True)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Trunk',
        ),
    ]
