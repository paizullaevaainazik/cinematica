# Generated by Django 4.2.4 on 2023-09-19 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('working_schedule', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('contacts', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.IntegerField(choices=[(1, 'Ongoing'), (2, 'Upcoming'), (3, 'Exited')], default=2)),
                ('age_limit', models.CharField(max_length=50)),
                ('start_movie', models.DateTimeField()),
                ('end_movie', models.DateTimeField()),
                ('image', models.ImageField(null=True, upload_to='movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.cinema')),
            ],
        ),
        migrations.CreateModel(
            name='RooMFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ShowTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
                ('movie_format', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.movieformat')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.room')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_seat', models.CharField(max_length=50)),
                ('number_of_row', models.CharField(max_length=50)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.room')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='format',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.roomformat'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.seat')),
                ('show_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.showtime')),
            ],
        ),
    ]