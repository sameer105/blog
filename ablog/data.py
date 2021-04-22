def Profile_data():
    from ablog.models import Profile, User
    for i in range(1,1001):
        user_id = User.objects.get(id =i)
        first_name = user_id.first_name
        last_name = user_id.last_name
        bio = 'Hey',first_name,'this side'
        website_url = 'www.',first_name,'/website.com'
        facebook_url = 'www.',last_name,'/facebook.com'
        twitter_url = 'www.',first_name,'/twitter.in'
        instagram_url = 'www.', last_name,'/instagram.in'

        p1 = Profile(user=user_id, bio=bio,
                     website_url=website_url, facebook_url=facebook_url, twitter_url=twitter_url,
                     instagram_url=instagram_url, pinterest_url='www.google.com')
        p1.save()

def Post_data():
    for i in range(1,1001):
        from ablog.models import Post,User
        user_id = User.objects.get(id=i)
        first_name = user_id.first_name
        email = user_id.email
        last_name = user_id.last_name
        title = first_name, "'s first blog"
        title_tag = last_name, "'s blog"
        author = User.objects.get(id=i)
        body = 'This is my first blog. My First name is', first_name,'My last name is', last_name, 'My email id is', email
        snippet = '-------'
        p1=Post(title=title,title_tag=title_tag,author=author,body=body,snippet=snippet)
        p1.save()




