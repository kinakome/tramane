from django.db import models

# Create your models here.

class User(models.Model):

    SEX_SELECT = (
        ('男性', '1: 男性'),
        ('女性', '2: 女性'),
        ('その他', '3: その他'),
    )

    user_name = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    password = models.CharField(max_length=8)
    sex = models.IntegerField(max_length=2, choices=SEX_SELECT)
    living = models.ForeignKey(Prefecture, on_delete=models.CASCADE)
    email = models.EmailField(max_length=240)

    def __str__(self):
        return self.user_name


class Trip(models.Model):
    posted_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.IntegerField(default=0, null=True)
    date_from = models.DateField()
    date_to = models.DateField()
    duration = models.DurationField()
    tags = models.ManyToManyField('Hashtag',blank=True)


    def __str__(self):
        return self.id


class Prefecture(models.Model):

    PREFECTURE_SELECT = (
        ('北海道', '1: 北海道'),('青森', '2: 青森'),('秋田', '3: 秋田'),('岩手', '4: 岩手'),('山形', '5: 山形'),
        ('宮城', '6: 宮城'),('福島', '7: 福島'),('新潟', '8: 新潟'),('富山', '9: 富山'),('石川', '10: 石川'),
        ('福井', '11: 福井'),('東京', '12: 東京'),('神奈川', '13: 神奈川'),('埼玉', '14: 埼玉'),('群馬', '15: 群馬'),
        ('栃木', '16: 栃木'),('茨城', '17: 茨城'),('千葉', '18: 千葉'),('山梨', '19: 山梨'),('静岡', '20: 静岡'),
        ('長野', '21: 長野'),('岐阜', '22: 岐阜'),('愛知', '23: 愛知'),('三重', '24: 三重'),('滋賀', '25: 滋賀'),
        ('京都', '26: 京都'),('大阪', '27: 大阪'),('兵庫', '28: 兵庫'),('奈良', '29: 奈良'),('和歌山', '30: 和歌山'),
        ('鳥取', '31: 鳥取'),('島根', '32: 島根'),('岡山', '33: 岡山'),('広島', '34: 広島'),('山口', '35: 山口'),
        ('徳島', '36: 徳島'),('香川', '37: 香川'),('愛媛', '38: 愛媛'),('高知', '39: 高知'),('福岡', '40: 福岡'),
        ('佐賀', '41: 佐賀'),('長崎', '42: 長崎'),('大分', '43: 大分'),('熊本', '44: 熊本'),('宮崎', '45: 宮崎'),
        ('鹿児島', '46: 鹿児島'),('沖縄', '47: 沖縄'),
    )

    prefecture = models.CharField(max_length=3, choices=PREFECTURE_SELECT)

    def __str__(self):
        return self.prefecture        


class Hashtag(models.Model):
    hashtag = models.CharField(max_length=10, null=True)
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.id
        


class Comment(models.Model):
    comment = models.TextField(max_length=300)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Picture(models.Model):
    picture = models.ImageField(upload_to='documents/', default='defo')
    trip = models.ForeignKey(Trip, related_name='pictures', on_delete=models.CASCADE)

    def __str__(self):
        return self.id