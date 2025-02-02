# Generated by Django 4.2.1 on 2024-05-09 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('discountPercentage', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=10000)),
                ('numberOfPeopleRated', models.IntegerField(default=0)),
                ('stock', models.IntegerField()),
                ('brand', models.CharField(max_length=120)),
                ('category', models.CharField(max_length=120)),
                ('thumbnail', models.URLField(blank=True, null=True)),
                ('images', models.ManyToManyField(blank=True, related_name='products', to='prod.image')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='prod.product'),
        ),
    ]
