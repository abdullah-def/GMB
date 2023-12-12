from lotus.models import Article



def return_articals():

    artical = Article.objects.all()[:10]

    return artical