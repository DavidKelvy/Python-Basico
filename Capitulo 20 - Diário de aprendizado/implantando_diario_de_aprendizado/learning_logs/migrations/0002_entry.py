# Gerado por Django 4.1b1 em 01/07/2022 03:28

# Requisitos: pip install django
# Import: from django.db import migrations, models
from django.db import migrations, models
# Requisitos: pip install django
# Import: import django.db.models.deletion
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_logs.topic')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
