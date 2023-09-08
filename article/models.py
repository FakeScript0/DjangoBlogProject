from django.db import models
from ckeditor.fields import RichTextField
class Article(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar:")
    title=models.CharField(max_length=45,verbose_name="Basliq:")
    content=RichTextField()
    created_date=models.DateTimeField(auto_now=True)
    article_image=models.FileField(blank =True,null=True,verbose_name="Sekil Elave Et")
    def __str__(self):
        return self.title#bele birsey etdikde ozelliye getmeden evvel neye gore siralayacaq
#burda classi yaratdiqdan sonra mutleq settings.pyde qurulan qovluqun yeni articlenin adi created_apps yerinde yazilmalidi
# Create your models here.
    class Meta:
        ordering=["-created_date"]
class Comment(models.Model):
    article=models.ForeignKey(Article,verbose_name="Makale",on_delete=models.CASCADE,related_name="comments")
    comment_author=models.CharField(verbose_name="Ad",max_length=80)
    comment_content=models.CharField(verbose_name="Yorum",max_length=300)
    comment_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_author
    class Meta:
        ordering=["-comment_date"]
