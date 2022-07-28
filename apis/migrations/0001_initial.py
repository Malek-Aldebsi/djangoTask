# Generated by Django 4.0.3 on 2022-07-26 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_ons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cost', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fp_percentage', models.DecimalField(decimal_places=2, max_digits=4)),
                ('partner_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('username', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Brand')),
                ('talabat_commission', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('careem_commission', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('cs_mena_subscription', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('ask_paper_subscription', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brand_branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('talabat_name', models.CharField(max_length=100)),
                ('carem_id', models.IntegerField()),
                ('csmena_name', models.CharField(max_length=50)),
                ('askpaper_name', models.CharField(max_length=50)),
                ('multiplayer_forecast', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(blank=True, null=True, upload_to='channel')),
            ],
        ),
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Fp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='FP')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Fp__',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('cost', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Knowleddge_center_section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Liability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('date_time', models.DateField(null=True)),
                ('type', models.CharField(max_length=50, null=True)),
                ('total', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('delivery_zone', models.CharField(max_length=50, null=True)),
                ('details', models.CharField(max_length=500, null=True)),
                ('customer_name', models.CharField(max_length=50, null=True)),
                ('customer_mobile_number', models.CharField(max_length=50, null=True)),
                ('payment_fees', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('delivary_fee', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('payment_method', models.CharField(max_length=50, null=True)),
                ('brand_branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='apis.brand_branch')),
                ('channel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='apis.channel')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='apis.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.order')),
            ],
        ),
        migrations.CreateModel(
            name='Type_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('rating', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.CharField(blank=True, max_length=15, null=True)),
                ('Brand_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.brand_branch')),
                ('channel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.channel')),
            ],
        ),
        migrations.CreateModel(
            name='Order_item_add_ons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('Add_ons', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.add_ons')),
                ('order_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.order_item')),
            ],
        ),
        migrations.CreateModel(
            name='Opening_hours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('brand_branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.brand_branch')),
                ('day', models.ManyToManyField(to='apis.days')),
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('status', models.BooleanField()),
                ('soft_delete', models.BooleanField()),
                ('brand_branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.brand_branch')),
                ('channel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.channel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Knowledge_center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('video_link', models.URLField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('fp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.fp')),
                ('knowledge_center_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.knowleddge_center_section')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='kitchefy_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postion', models.CharField(max_length=40)),
                ('role', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Incident_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('case_date_time', models.DateTimeField(null=True)),
                ('message', models.CharField(blank=True, max_length=100, null=True)),
                ('pdf_link', models.URLField(blank=True, null=True)),
                ('brand_branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.brand_branch')),
                ('channel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.channel')),
                ('liability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.liability')),
                ('type_rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.type_rating')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fp_branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('long', models.DecimalField(decimal_places=6, max_digits=9)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=20)),
                ('bilding_no', models.CharField(max_length=20)),
                ('active', models.BooleanField()),
                ('multiplayer_forecast', models.DecimalField(decimal_places=3, max_digits=5)),
                ('sales_tax', models.DecimalField(decimal_places=3, max_digits=5)),
                ('revenue_percentage', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('fp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.fp')),
            ],
        ),
        migrations.AddField(
            model_name='brand_branch',
            name='Fp_branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand_branch', to='apis.fp_branch'),
        ),
        migrations.AddField(
            model_name='brand_branch',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branch', to='apis.brand'),
        ),
        migrations.CreateModel(
            name='Announcement_center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('brand_branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.brand_branch')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]