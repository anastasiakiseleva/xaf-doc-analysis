---
uid: "405418"
title: 'Update Database Schema and Migrations in EF Core'
---
# Update Database Schema and Migrations in EF Core

When you develop an application (in Debug mode) you can use the following options to update database schema when the structure of business objects changes:

* [Automatic Database Schema Update](#automatic-database-schema-update) _(default behavior)_  
XAF automatically updates database schema when you change the data model of your application.
* [EF Core Migrations](#ef-core-migrations)  
You can manually generate and apply [migrations](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations) to a database every time you change the data model of your application.

To update the production database, run the XAF application with specific command line parameters. See the following help topic for additional information: <xref:113239>.

## Automatic Database Schema Update

In Debug mode, XAF automatically updates database schema when the structure of business objects changes. For instance, when you add a new business class or a property, or remove a property, XAF can create missing tables, add or remove columns, indexes, etc.

> [!important]
> Note that you can lose data if you delete columns, change column types, delete/recreate indexes, or otherwise modify the database.
> 
> We recommend that you use automatic database schema update with **test databases**. Be prepared to lose and recreate data frequently. 

In a [multi-tenant application](xref:404436), login to every tenant to let XAF automatically update that tenant's database schema.

### Limitations

The database schema update mechanism is based on the [standard functionality of EF Core](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations). EF Core limitations are reflected in the update mechanism.

* If a table contains data, table update can fail. For instance, if you change a column type and it does not match the type of existing data.
* The XAF automatic update mechanism has the same scenario limitations as the functionality of standard EF Core migrations.
* If you want to use EF Core migrations, automatic database schema updates cannot be active.

### Disable Automatic Updates

You can disable automatic database schema updates for a particular object space provider in ApplicationBuilder:  

File: _MySolution.Blazor.Server\BlazorApplication.cs_ or _MySolution.Win\Program.cs_

```csharp
builder.ObjectSpaceProviders
    .AddEFCore(options => options.SchemaUpdateOptions.DisableUpdateSchema = true)
    .WithDbContext<...>(...)
    // ...
```

## EF Core Migrations

> [!note]
> If you use EF Core migrations in your project, [disable the automatic database schema update](#disable-automatic-updates) since it can disrupt migrations.

[Migrations](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations) are native to EF Core. They allow you to manually update the database schema and keep it in sync with the application's data model while preserving existing data.

Before you run the application for the first time, or anytime after you change the data model, you need to generate a migration and then apply it to the database.

### Set Up Migrations

> [!IMPORTANT]
> Delete the existing database (if there is one) before you proceed, because Entity Framework Core does not take the existing database schema into consideration when it generates the first migration.

1. Add the **Microsoft.EntityFrameworkCore.Tools** NuGet package to the **YourProjectName.Module** project and build the solution. 

    The package's version must match the version of Entity Framework Core supported in XAF. [!include[](~/templates/efcoreversion.md)]

2. In the **YourProjectName.Module** project, go to the _BusinessObjects_ folder and open the _YourProjectNameDbContext.cs_ file. Replace the declaration of the `YourProjectNameDesignTimeDbContextFactory` class with the following code snippet:

   ```csharp
   namespace YourProjectName.Module.BusinessObjects;
   //...
   public class YourProjectNameDesignTimeDbContextFactory : DesignTimeDbContextFactory<YourProjectNameDbContext> {
      protected override string ConnectionString  => 
        "Integrated Security=SSPI;Pooling=false;Data Source=(localdb)\\mssqllocaldb;Initial Catalog=YourProjectName";
      }
   }
   ```

3. In Visual Studio, open the **Package Manager Console** and use the following command to add a migration:

    ```Console
    add-migration MyInitialMigrationName -StartupProject "YourProjectName.Module" -Project "YourProjectName.Module"
    ```


4. Update the database with the following command:

    ```Console
    update-database -StartupProject "YourProjectName.Module" -Project "YourProjectName.Module"
    ```
Note that in a [multi-tenant application](xref:404436), you should apply a migration to every tenant database. Refer to the following topic for additional details: <xref:405376>.

Update the database if you add, rename, or delete a class/property, or if you otherwise change the data model in your application. To do this, repeat steps 3 and 4 of this tutorial.  Make sure to use a unique migration name for each new migration.
