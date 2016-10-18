Title: How to create a blog post (Markdown)
Date: 2016-10-16 10:28
Modified: 
Author: Steve Gregg
Category: General
Tags: blog

There are two ways to create a new blog post here at Python Monthly. The first and easiest way is to use our Python Script, 'new_post.py'. This method does require that you have Python 3 installed and have downloaded or cloned the 'Python-Monthly-Website' repository. First navigate to the root of the 'Python-Monthly-Website' folder from the command line, call the script and pass your blog post as an argument as shown below

`$ python new_post.py "My new blog post title"`

This generates a file in the 'content' folder with the date and blog post title (2016_10_16_my-new-blog-post-title.md). Open the file in your favorite text editor. The file should contain the following

```
Title: My new blog post title
Date: 2016-10-16 10:28
Modified: 
Author: 
Category: 
Tags: 
```
