from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(default=None)),
                ('address', models.TextField()),
                ('reg_date', models.DateField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('amount', models.IntegerField()),
                ('add_date', models.DateField(auto_now=True)),
                ('description', models.TextField(default='Место для описания')),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(
                    decimal_places=2, max_digits=8)),
                ('date_ordered', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='app1.client')),
                ('products', models.ManyToManyField(to='app1.product')),
            ],
        ),
    ]
