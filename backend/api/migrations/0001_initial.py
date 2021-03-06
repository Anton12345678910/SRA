# Generated by Django 3.0.7 on 2020-06-23 20:25

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', api.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('año_nacimiento', models.SmallIntegerField(default=0)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('año_ingreso', models.SmallIntegerField(default=0)),
                ('semestre_ingreso', models.SmallIntegerField(default=1)),
                ('carrera_origen', models.TextField(blank=True)),
                ('copia_registro', models.FileField(null=True, upload_to='uploads/%Y/%m/%d/')),
                ('fecha_registro', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('estado_actual', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_asignatura', models.SmallIntegerField(default=0)),
                ('glosa', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('hora', models.SmallIntegerField(default=0)),
                ('interes', models.BooleanField(default=False)),
                ('medio_contacto', models.CharField(max_length=40)),
                ('autogestion', models.BooleanField(default=True)),
                ('nombre_contacto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Administrador',
            },
            bases=('api.user',),
            managers=[
                ('objects', api.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Reunion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('hora', models.SmallIntegerField(default=0)),
                ('realizacion', models.BooleanField(default=False)),
                ('cumplimiento_objetivos', models.BooleanField(default=False)),
                ('medio_reunion', models.CharField(max_length=50)),
                ('observaciones', models.TextField(default='')),
                ('iniciales_academico', models.CharField(default='', max_length=10)),
                ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Contacto')),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.SmallIntegerField(default=2010)),
                ('semestre', models.SmallIntegerField(default=1)),
                ('tipo_causal', models.IntegerField(default=0)),
                ('asignaturas_reportadas', models.SmallIntegerField(default=0)),
                ('prioridad', models.SmallIntegerField(default=0)),
                ('observacion', models.CharField(default='', max_length=50)),
                ('reiteraciones_causal', models.SmallIntegerField(default=0)),
                ('tipo_ingreso', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Recomendacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.SmallIntegerField()),
                ('estado', models.CharField(default='', max_length=10)),
                ('reunion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Reunion')),
            ],
        ),
        migrations.CreateModel(
            name='Problema_asociado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.SmallIntegerField()),
                ('explicacion', models.TextField(default='')),
                ('estado', models.CharField(default='', max_length=10)),
                ('reunion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Reunion')),
            ],
        ),
        migrations.CreateModel(
            name='Derivacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entidad_derivacion', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('observacion', models.TextField(blank=True)),
                ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Contacto')),
            ],
        ),
        migrations.AddField(
            model_name='contacto',
            name='reporte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Reporte'),
        ),
        migrations.CreateModel(
            name='Causal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.SmallIntegerField(default=2010)),
                ('tipo', models.SmallIntegerField(default=0)),
                ('condiciones', models.TextField(blank=True, null=True)),
                ('reporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Reporte')),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura_reportada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asistencia', models.SmallIntegerField(default=0)),
                ('participacion', models.SmallIntegerField(default=1)),
                ('notas_ponderadas', models.SmallIntegerField(default=1)),
                ('año_semestre', models.IntegerField(default=12010)),
                ('observaciones', models.TextField(blank=True)),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Asignatura')),
                ('reporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Reporte')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('jornada', models.SmallIntegerField(blank=True, null=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Administrador')),
            ],
            options={
                'verbose_name': 'Profesor',
            },
            bases=('api.user',),
            managers=[
                ('objects', api.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Coordinador',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Administrador')),
            ],
            options={
                'verbose_name': 'Coordinador',
            },
            bases=('api.user',),
            managers=[
                ('objects', api.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='asignatura',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Profesor'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='coordinador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Coordinador'),
        ),
    ]
