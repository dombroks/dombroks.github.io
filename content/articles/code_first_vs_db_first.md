---
title: "Code First Approach vs. Database First Approach"
date: 2023-05-20
image: "img/code_vs_db.webp"
context: "Coding | Database"
ReadingTime: 4
draft: false
brief: "Choosing the Right Path: Code-First and Database-First Approaches in Software Development."
slug: "Code First Approach vs. Database First Approach"
---


[Image Source](https://unsplash.com/photos/pKeF6Tt3c08)

We were working on a project for a big company using C# as a programming language and Entity framework as an ORM, both of these technologies are supported by Microsoft.

Entity Framework is an open-source object-relational mapping framework for ADO .NET, which is a data access technology, this means that you can use this technology to access data in the database. For C#, we all know what C# is.

As a team, we were discussing whether we choose the code-first approach or the database-first approach. So, what are these approaches?

Let me explain some things to you before we go to the code-first and the database-first approaches, **DbContext** and **DbSet.** A DbContext is a class that act as a bridge between your data models and the database, it is responsible for maintaining the state of the database and providing a way to interact with it through the application. It is also responsible for tracking changes in the database and saving them to the database. It contains the configuration information that defines how the entities are mapped to the database schema. This configuration includes entity types, mapping between entities and tables, relationships between entities, and any constraints or validations. A DbSet property represents each table or a view in the database, these properties are used to query, update, insert, or delete data from a specific database table.

### **Code first approach**

The code-first approach is a way to design your application’s data models by creating them as C# classes for your models and then you use them to create your database. This way, you can focus on designing your domain models and the entity framework will handle the database creation.

As we said, the entity framework will handle the creation of your database or the mapping to an existing database starting from the models you created.

In order to apply the code-first approach, you need to follow these steps:

*   Define your model classes, each class corresponds to a table in your database.
*   Create a DbContext class that inherits from the DbContext class provided by Entity Framework.
*   Enable migrations, this way you can update the database schema so that the database and your models are still in sync. Use the package manager console to enable the migrations, use the **Enable-Migrations** command to do that, and create a migration with the **Add-Migration <MigrationName>** command.
*   Create the database, through the package manager console, use the entity framework to create the database and the table. Also, you need to write a command for that which is the **Update-Database** command.

Note: to open the package manager console in the visual studio, go to `Tools` > `NuGet Package Manager` > `Package Manager Console`.

As a simple example, we will create a Person model class and a DbContext class:

```C#
public class Person  
{  
    public int Id { get; set; }  
    public string FullName { get; set; }  
    public int Age { get; set; }  
}

public class MyDbContext : DbContext  
{  
    public DbSet<Person> Persons { get; set; }  
  
    public MyDbContext() : base("TheConnectionString")  
    {  
    }  
}
```

Here, you might notice that we have passed a string called the connectionString, it is a string of parameters that provides the necessary information to establish a connection to a data source. It contains information about the data source, such as the server's name, database name, and authentication credentials.

An example of a connection string would be:

Data Source=myServerAddress;Initial Catalog=myDataBase;User ID=myUsername;Password=myPassword;

*   `Data Source`: The name or network address of the instance of SQL Server to connect to.
*   `Initial Catalog`: The name of the database to connect to.
*   `User ID`: The user ID to use when connecting to the data source.
*   `Password`: The password to use when connecting to the data source.

What code first approach brings to the table?

*   It adds more speed to the development process. Devs can focus on the business logic and modeling data and then automatically generate the database schema.
*   You don’t have to edit the database after you made a change to your model since they are in sync with each other, and every change is tracked.
*   It aligns well with Agile development.

### Database First approach

The database first approach is a way to create the data models starting from an existing database. We generate our data models and the DbContext class based on an existing database schema. You start by creating a database including the tables, their properties, and the relations between them. To create a database, you can use the Microsoft SQL Server Studio (I love that tool).

In order to apply the database first approach, you need to follow these steps:

*   Create/Attach your database.
*   Use the entity framework to generate the necessary files for you.
*   Use the generate files (Entity and DbContext classes).

An example of how to query data using the DbContext would be like this:
```C#
public IEnumerable<Person> GetPersons()  
        {  
            using (myDBContext con = new MyDBContext())  
            {  
                con.Persons.Load();  
                return con.Persons.Local.ToList();  
            }  
        }
```

What database first approach brings to the table?

*   It helps you when you have a complex database schema.
*   It gives the ability to use an existing database schema.
*   You will be supported by tools like the Microsoft SQL Server Studio which I like to use.

By [Younes Belouche](https://medium.com/@younes_belouche) on [May 20, 2023](https://medium.com/p/a3830c0cc9b6).

[Medium link](https://medium.com/@younes_belouche/code-first-approach-vs-database-first-approach-a3830c0cc9b6)

