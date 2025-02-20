---
title: "N + 1 Queries Problem (A Django example)"
date: 2022-08-30
image: "img/n+1.webp"
context: "Performance | Django"
ReadingTime: 3
draft: false
brief: "A serious performance issue."
slug: "N + 1 Queries Problem (A Django example)"
---
Image from Unsplash by Markus Winkler

In this post, we will learn about N + 1 Queries Problem, what is it and how to solve it.

### **What is the N + 1 Queries Problem?**

In short, the N + 1 Queries Problem is a performance anti-pattern that happens when a query is executed for every result you got from a previous query. **N** here is the number of queries for every result you got from the first query. This means if we executed a query and we got 200 results, then N + 1 = 201 queries.

Let’s see an example to get familiar with the problem. Suppose we have this code:

```Python
posts = Post.objects.order_by("created_on")
for post in posts:
  print(post.title, "written by", post.author)
```

In this simple example, we have posts QuerySet and a for loop that iterates over it and prints the title and the author for every single post. By looking at the code, you figure out that we have a Post model and an Author model. This tells you that author attribute is a foreign key.

Let’s see how much query our code performs:

First, we’ve created the **Post** QuerySet, so till now, we have 0 queries executed. Why? because QuerySets are lazy. I quote from the Django documentation:

> _“QuerySets are lazy – the act of creating a_ `_QuerySet_` _doesn’t involve any database activity. You can stack filters together all day long, and Django won’t actually run the query until the_ `_QuerySet_` _is evaluated.”_

You can read more about this form [here](https://docs.djangoproject.com/en/4.1/topics/db/queries/#querysets-are-lazy).

Then we iterate over the posts, this will lead the QuerySet to evaluate and fetch its results. Now, we have 1 query.

After that, we print the title and the author corresponding to the post. Since the title is a field on the Post itself, we will have no extra queries because it has been fetched in the first query. But what about the author? we remember that it is a foreign key, so Django didn’t fetch it. Therefore, Django will do extra work by executing another query to fetch the corresponding name for the given author_id (Obviously, the Author model contains a name field).

By now, we have executed **1** query to get the posts, and **N** queries to get the authors. **N** is the number of posts.

Imagine the case where we have 1 million posts 😆.

### How to tackle this problem?

**select_related()** and **prefetch_related()** are two QuerySet methods that provide a solution to tackle the N+1 Queries Problem.

[**select_related()**](https://docs.djangoproject.com/en/4.1/ref/models/querysets/#django.db.models.query.QuerySet.select_related) returns a QuerySet with selecting additional related-object data when it executes its query. After using this method, our previous code will be like this:

```Python
posts = Post.objects.order_by("created_on").select_related("author")
for post in posts:
    print(post.title, "written by", post.author.name)
```

Now we have only **1** query that selects both posts and their related authors.

[**prefetch_related**](https://docs.djangoproject.com/en/4.1/ref/models/querysets/#django.db.models.query.QuerySet.prefetch_related)**()** returns a QuerySet that will automatically retrieve, in a single batch, related objects for each of the specified lookups. Now the code will look like this:

```Python
posts = Post.objects.order_by("created_on").prefetch_related("author")
for post in posts:
    print(post.title, "written by", post.author.name)
```

The difference between the two methods is that **select_related()** creates an SQL join and includes the related-object data in the SELECT statement. It is only suitable for foreign key and one-to-one relationships. On the other hand, **prefetch_related()** does a separate lookup for each relationship and uses Python to perform joins. This enables us to prefetch all kinds of relationship objects, which are: _many-to-many, many-to-one, foreign key, and one-to-one relationships._

There are tools that permit you to find N + 1 Queries Problem but I will not cover them for the sack of this post shortness.

Thanks for reading this article ❤

Connect with me on [Linkedin](https://www.linkedin.com/in/younes-belouche-641bb3197/), [Instagram](https://www.instagram.com/younes_belouche/) and [Github](https://github.com/dombroks).

By [Younes Belouche](https://medium.com/@younes_belouche) on [August 30, 2022](https://medium.com/p/fd57e3a1761e).

[Medium link](https://medium.com/@younes_belouche/n-1-queries-problem-a-django-example-fd57e3a1761e)

