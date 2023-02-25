# Generated by Django 4.1.5 on 2023-02-13 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0003_alter_client_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produits', '0002_produit_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Qnt_Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qnt', models.PositiveIntegerField()),
                ('credit', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='credit.credit')),
                ('produit', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='produits.produit')),
            ],
        ),
    ]
