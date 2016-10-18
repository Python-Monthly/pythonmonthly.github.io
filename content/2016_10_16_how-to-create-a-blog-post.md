Title: How to create a blog post
Date: 2016-10-16 10:28
Modified: 
Author: Steve Gregg
Category: General
Tags: blog

There are two ways to create a new blog post here at Python Monthly. The first and easiest way is to use our Python Script, 'new_post.py'. This method does require that you have Python 3 installed and have downloaded or cloned the 'Python-Monthly-Website' repository. First navigate to the root of the 'Python-Monthly-Website' folder from the command line, call the script and pass your blog post title as an argument as shown below

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

Add your name to the 'author' field and also fill in the 'Category' and 'Tags' fields. Below these headers, you may begin the body of your post.

The second way to create a blog post is to manually do what the Python script does, ie launch your favorite text editor and paste the following text

```
Title: My new blog post title
Date: 2016-10-16 10:28
Modified: 
Author: 
Category: 
Tags: 
```

Just as the first method above, add your name to the 'author' field and also fill in the 'Category' and 'Tags' fields. You may then begin the body of your post below the headers.


### Things to note:###

* The 'Modified' field is optional and is used to show when a post was updated
* The time in the 'Date' field is optional
* The 'Category' field is used to categorize posts by topic. If you are unsure of a category, you can use the 'General' category
* The 'Tags' field is also optional and is used to tag your post with keywords.




