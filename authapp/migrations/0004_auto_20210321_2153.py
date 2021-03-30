
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


def add_user_profiles(apps, schema_editor):
    User = apps.get_model('authapp', 'User')
    ShopUserProfile = apps.get_model('authapp', 'ShopUserProfile')
    users = User.objects.all()
    for user in users:
        user_profile = ShopUserProfile.objects.create(user=user)
        user_profile.save()


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20210321_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 23, 19, 53, 6, 162280, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='ShopUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(blank=True, max_length=128, verbose_name='теги')),
                ('aboutMe', models.TextField(blank=True, max_length=512, verbose_name='о себе')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Мужской'), ('W', 'Женский')], max_length=1, verbose_name='пол')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(add_user_profiles)
    ]
