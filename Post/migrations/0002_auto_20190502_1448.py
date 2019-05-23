# Generated by Django 2.2 on 2019-05-02 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reaction',
            name='reaction_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Citizen'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Citizen'),
        ),
        migrations.AddField(
            model_name='pictures',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Post.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Citizen'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Post.Post'),
        ),
    ]
