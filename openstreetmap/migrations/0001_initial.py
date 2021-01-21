# Generated by Django 3.1.5 on 2021-01-20 18:11

from django.db import migrations, models
import osm_field.fields
import osm_field.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyOsm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', osm_field.fields.OSMField(lat_field='location_lat', lon_field='location_lon')),
                ('location_lat', osm_field.fields.LatitudeField(validators=[osm_field.validators.validate_latitude])),
                ('location_lon', osm_field.fields.LongitudeField(validators=[osm_field.validators.validate_longitude])),
            ],
        ),
    ]
