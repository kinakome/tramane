from django.db import models

# Create your models here.

class User(models.Model):

    SEX_SELECT = (
        ('男性', '男性'),
        ('女性', '女性'),
    )

    user_name = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    password = models.CharField(max_length=8)
    sex = models.CharField(max_length=2, choices=SEX_SELECT)
    password = models.CharField(max_length=8)
    living = models.ForeignKey(Prefecture, on_delete=models.CASCADE)
    email = models.EmailField(max_length=240)

    def __str__(self):
        return self.user_name


class Trip(models.Model):
    posted_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.IntegerField(default=0)
    date_from = models.DateField()
    date_to = models.DateField()
    duration = models.DurationField()
    tags = models.ManyToManyField('Hashtag',blank=True)


    def __str__(self):
        return self.id


class Prefecture(models.Model):

    PREFECTURE_SELECT = (
        ('北海道', '北海道'),('青森', '青森'),('秋田', '秋田'),('岩手', '岩手'),('山形', '山形'),
        ('宮城', '宮城'),('福島', '福島'),('新潟', '新潟'),('富山', '富山'),('石川', '石川'),
        ('福井', '福井'),('東京', '東京'),('神奈川', '神奈川'),('埼玉', '埼玉'),('群馬', '群馬'),
        ('栃木', '栃木'),('茨城', '茨城'),('千葉', '千葉'),('山梨', '山梨'),('静岡', '静岡'),
        ('長野', '長野'),('岐阜', '岐阜'),('愛知', '愛知'),('三重', '三重'),('滋賀', '滋賀'),
        ('京都', '京都'),('大阪', '大阪'),('兵庫', '兵庫'),('奈良', '奈良'),('和歌山', '和歌山'),
        ('鳥取', '鳥取'),('島根', '島根'),('岡山', '岡山'),('広島', '広島'),('山口', '山口'),
        ('徳島', '徳島'),('香川', '香川'),('愛媛', '愛媛'),('高知', '高知'),('福岡', '福岡'),
        ('佐賀', '佐賀'),('長崎', '長崎'),('大分', '大分'),('熊本', '熊本'),('宮崎', '宮崎'),
        ('鹿児島', '鹿児島'),('沖縄', '沖縄'),
    )

    prefecture = models.CharField(max_length=3, choices=PREFECTURE_SELECT)

    def __str__(self):
        return self.prefecture        


class Hashtag(models.Model):
    hashtag = models.CharField(max_length=10)
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id
        


class Comment(models.Model):
    comment = models.CharField(max_length=300)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Picture(models.Model):
    picture = models.ImageField(upload_to='documents/', default='defo')
    trip = models.ForeignKey(Trip, related_name='pictures', on_delete=models.CASCADE)

    def __str__(self):
        return self.id