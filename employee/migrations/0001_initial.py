from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('employment_position', models.CharField(max_length=200)),
                ('employment_start_date', models.DateTimeField()),
                ('salary', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('employment_photo', models.ImageField(blank=True, help_text='150x150px', upload_to='images/%Y/%m/%d', verbose_name='employment_photo')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='employee.Employee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
