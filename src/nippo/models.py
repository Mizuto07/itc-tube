from django.db import models

class NippoModel(models.Model):
    title = models.CharField(max_length=100) # charfieldはテキスト
    content = models.CharField(max_length=1000) # max_lengthは書き込める最大文字数 255推奨
    timestamp = models.DateTimeField(auto_now_add=True) # 日付と時間を書きこむ
    # auto_now_addをtrueで自動で今の時刻を書き込む

    def __str__(self):
        return self.title
