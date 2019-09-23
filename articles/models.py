from django.db import models

# Reporter - Article 관계에서 reporter가 여러 글을 쓰므로
# 1:N 관계임
# reporter - name
class Reporter(models.Model):
    name = models.CharField(max_length=10)


class Article(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # reporter = models.ForeignKey(Reporter, on_delete=models.PROTECT)

# Article(1) - Comment(N)
# comment - content
class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
