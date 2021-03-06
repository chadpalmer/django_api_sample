# Generated by Django 3.0.2 on 2020-01-05 05:12

import axioms.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('axioms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('footer', models.CharField(blank=True, default='', max_length=500)),
            ],
            bases=(axioms.models.SingleInstanceMixin, models.Model),
        ),
        migrations.AlterField(
            model_name='axiom',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='axioms', to=settings.AUTH_USER_MODEL),
        ),
    ]
