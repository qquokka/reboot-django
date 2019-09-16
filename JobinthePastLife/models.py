from django.db import models

class PastLife(models.Model):
    name = models.CharField(max_length=4)
    job = models.CharField(max_length=20)
    birthday = models.CharField(max_length=15)

# Reporter - Article 관계에서 reporter가 여러 글을 쓰므로
# 1:N 관계임
# reporter - name

# Article(1) - Comment(N)
# comment - content