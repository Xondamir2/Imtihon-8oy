# Generated by Django 5.0.6 on 2024-06-13 15:46

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mother_name', models.TextField(help_text='onasini ismi')),
                ('father_name', models.TextField(help_text='otasini ismi')),
                ('familiy_number', models.IntegerField(help_text='oilada nechtasizlar')),
            ],
        ),
        migrations.CreateModel(
            name='SendStudentMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='teachers/')),
                ('full_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('experience', models.IntegerField(help_text='tajribasi /yil')),
                ('knowledge', models.CharField(help_text='misol: Python', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(upload_to='students/')),
                ('qurilma', models.CharField(help_text='qanday qurilma ishlatishi', max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('the_border', models.BooleanField(default=False, help_text='chegaraga chiqanmisiz')),
                ('region', models.CharField(help_text='yashash joyi', max_length=150)),
                ('place_of_birth', models.CharField(help_text="tug'ilgan joy", max_length=150)),
                ('family', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='online.family')),
                ('teacher', models.ManyToManyField(to='online.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('student', models.ForeignKey(help_text='Studentni tanlash', on_delete=django.db.models.deletion.CASCADE, to='online.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentShikoyatlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('student', models.OneToOneField(help_text='Oquvchi', null=True, on_delete=django.db.models.deletion.SET_NULL, to='online.student')),
                ('teacher', models.ForeignKey(help_text='shikoyat bermoqchi bolgan ustoz', null=True, on_delete=django.db.models.deletion.SET_NULL, to='online.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('platform', models.CharField(help_text='qaysi platformada dars bolib otishi', max_length=150)),
                ('opening_time', models.DateTimeField(auto_now_add=True)),
                ('closing_time', models.DateTimeField(blank=True, null=True)),
                ('graduate', models.BooleanField(default=False, help_text='guruh bitirildimi ? ')),
                ('duration', models.DecimalField(decimal_places=2, help_text='course davomiyligi', max_digits=10)),
                ('kunlar', models.CharField(help_text='dars kunlari', max_length=155)),
                ('student', models.ManyToManyField(to='online.student')),
                ('teacher', models.ManyToManyField(to='online.teacher')),
                ('topics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online.topics')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherHomework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(help_text='homework.png', upload_to='teacher_homework/')),
                ('video', models.FileField(blank=True, help_text='dars videosi', null=True, upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'WMW'])])),
                ('time', models.DateTimeField(auto_now_add=True, help_text='uyga vazifa berilgan vaqt')),
                ('time_duration', models.DateTimeField(help_text='uyga vazifa davomiyligi')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='online.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='StudentHomework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homework', models.ImageField(blank=True, null=True, upload_to='student_homework/')),
                ('time', models.DateTimeField(auto_now_add=True, help_text='oquvchi uyga vazifa qilgan vaqt')),
                ('description', models.CharField(max_length=255)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='online.student')),
                ('teacherhomework', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='online.teacherhomework')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baho', models.BooleanField(help_text='True dars yoqdi manosini bildiradi')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online.course')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='online.student')),
                ('topics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online.topics')),
            ],
        ),
    ]
