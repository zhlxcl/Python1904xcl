from django import forms
from .models import Article
from comment.models import Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","body"]
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control"})
        }
        labels = {
            "title":"文章标题",
            "body":"文章正文",
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name","email","url","content"]

