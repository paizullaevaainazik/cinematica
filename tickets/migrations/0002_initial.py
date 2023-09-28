# Generated by Django 4.2.4 on 2023-09-26 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0004_alter_movie_end_movie_alter_movie_start_movie'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='club_card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.clubcard'),
        ),
        migrations.AddField(
            model_name='tickets',
            name='seats',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.seat'),
        ),
        migrations.AddField(
            model_name='tickets',
            name='showtime',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.showtime'),
        ),
        migrations.AddField(
            model_name='tickets',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.tickettype'),
        ),
        migrations.AddField(
            model_name='tickets',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.cart'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
