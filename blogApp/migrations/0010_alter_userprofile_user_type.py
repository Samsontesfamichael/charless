

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0009_post_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.IntegerField(default=2),
        ),
    ]
