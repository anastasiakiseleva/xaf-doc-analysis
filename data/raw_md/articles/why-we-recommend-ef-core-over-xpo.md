---
uid: "404186"
title: Why We Recommend EF Core over XPO for New Development
owner: Andrey Kozhevnikov
seealso: []
---
# Why We Recommend EF Core over XPO for New Development

XAF supports two Object-Relational Mapping tools: [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/) and [DevExpress XPO](xref:1998). As you might expect, we often receive comparison requests from XAF UI and Web API Service users: which ORM should I choose? The answer, of course, depends on your tasks, and on how familiar you are with XPO and EF Core. Review the information in this topic to choose the ORM that suits your business needs best in the following scenarios: 

* You are new to our application frameworks, have no knowledge of either ORM, and do not yet know which one to choose.

* You are starting a new project, have experience with XPO or EF Core, and want to re-evaluate your choice due to ORM issues or new opportunities.

EF Core is the default choice in the [Template Kit](xref:405447) and [Getting Started](xref:113577) tutorials. This change was made because we consider EF Core to be the best choice for new XAF and Web API Service development.

## Should Existing XPO Users Migrate to EF Core

If you have experience with both ORMs and prefer XPO to EF Core, you can continue to use XPO even for new projects - there is no need to switch to EF Core. 

Reasons not to switch to EF Core include:

- We are proud of XPO and all that it offers; it is a mature ORM that we still use in several of our internal projects along with EF Core. New and existing DevExpress customers also continue to use XPO.

- We continue to develop new XAF and Web API Service features that meet user needs and market demand for XPO and EF Core (there is no "EF Core-First" policy for new XAF development). For instance, XPO supports different .NET Core / .NET versions, and is expected to support .NET vNext in the future. The new XAF Web API Service and Multi-Tenancy module also support XPO.

- We will continue to fix security and other XPO bugs (see [Version History](https://supportcenter.devexpress.com/versionhistory)), enhance XPO code, and update learning materials for XPO users.

When choosing an ORM, we advise that you evaluate the current ORM state as it relates to the issues and requirements of your projects.

## Compatibility Considerations on a Potential Migration from XPO to EF Core

To reiterate, DevExpress is not requiring nor asking our customers to migrate from XPO to EF Core. Migration considerations for new projects should be based on your strategic investment in .NET, its potential market changes and the growing popularity of EF Core (see below).

Note that XPO and EF Core are entirely different ORMs. These tools handle many things differently. For example, inheritance and database schemas for the same logically equal entities will be different for these ORMs with default settings. Business classes for these ORMs cannot be used with the same database tables. We did not plan to make these classes compatible (key type, table names, etc.). Applications cannot easily be moved from XAF to another ORM because of different table structures in their data models. Technically, it is possible to migrate your XAF code from one ORM to another, but you will also need to manually modify your table structure and migrate data. This requires a deep understanding of ORM internals and we do not consult on such matters.

## XPO vs EF Core: Similarities

{|
|-
! Aspect
! Comparison Result
|-
| Tools and Extensions
| Both [EF Core](https://learn.microsoft.com/en-us/ef/core/extensions/) and [XPO](xref:14809) support Code-First, Model-First, and Database-First development. Both include logging and profiling tools, a visual designer for the data model, and scaffolding tools that allow you to generate data model classes from existing databases.

EF Core has an advantage when it comes to available tools and extensions implemented by third parties or Microsoft. You can use a large set of paid extensions from DevArt, as well as built-in extensions in Microsoft frameworks and products such as Blazor, OData, Visual Studio, and so on.
|-
| Database Schema Migration
| [EF Core](xref:402971) and [XPO](xref:2632#important-notes) can update database structure after your data model structure changes.

In EF Core, XAF can automatically create missing tables, add or remove columns, change columns and indexes. Refer to the following topic for more information: <xref:405418>

XPO can automatically add tables and columns for new classes and properties. XPO does not modify existing tables, columns, indexes, or foreign keys, nor does it respond to property/column size or type changes, deletions, etc. Handle these changes manually using tools applicable to your database.
|-
| Performance
| EF Core and XPO show comparable performance in popular cases. Advanced scenarios may perform better with either EF Core or XPO. We cannot declare a clear winner in this category. 

Benchmarks: 

* [EF Core 7 vs XPO](https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/23.1.1+/Benchmarks)
* [EF Core 6 vs XPO](https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/22.2.4%2B/Benchmarks)
* [EF Core 8 vs XPO](https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/24.1.6%2B/Benchmarks)
* [EF Core 9 vs XPO](https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/24.2.3%2B/Benchmarks)
* [EF Core 10 vs XPO](https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/25.2.5%2B/Benchmarks)
* [Dapper.Tests.Performance](https://github.com/DapperLib/Dapper/tree/main/benchmarks/Dapper.Tests.Performance)

Both [EF Core](xref:404429) and [XPO](xref:2024) allow developers to control delayed/lazy, eager, and explicit loading of related data. Both ORMs support XAF’s [Data Access Modes](xref:113683), complex LINQ queries, LINQ data projections, aliased/calculated properties, and direct SQL calls.
|-
| XAF Module Support
| Popular XAF [modules](xref:118046) support EF Core and XPO. You can use the following modules with any ORM: **Security** (including Middle Tier Security[^1]), **Validation**, **Conditional Appearance**, **Reports**, **Audit Trail**, **File Attachments**, **Clone Object**, **Office**, **Dashboards**, and **Web API Service**.

Although XPO is a DevExpress ORM, XPO has no integration advantages when used with XAF or other DevExpress products. 

In 2023, we reached comparable levels of DevExpress Documentation and GitHub Examples that describe XAF integration with XPO or EF Core.  
|-
| Soft Deletion
| Both [EF Core](xref:405259) and [XPO](xref:2026#deferred-object-deletion) support soft and deferred object deletion. In this case, ORM marks objects as deleted and does not physically remove them from a database right away. This technique helps you avoid database exceptions when deleting objects referenced by other entities.
|-
| Data Filtering
| EF Core and XPO filtering capabilities are on par in terms of supported [CriteriaOperator and built-in criteria functions](xref:4928). Both ORM also support advanced [criteria features](xref:404016) such as Upcasting (Combine Data from Base and Derived Classes), Free Joins (Query Non-Associated Data & Calculate Aggregations), and Filter by Object Type.
|-
| Control Concurrency Conflicts
| Both EF Core and XPO support the [Optimistic Concurrency](xref:113596) control in XAF applications.
|-
| Base Entity Classes
| Both [EF Core](xref:DevExpress.Persistent.BaseImpl.EF.BaseObject) and [XPO](xref:113146) ship with built-in Base Persistent Classes (like BaseObject as part of the DevExpress.Persistent.BaseImpl.* [libraries](xref:112571)) that save time and lines of code for common scenarios with or without additional XAF modules.
|-
| Calculated/Computed Fields
| Both [EF Core](xref:DevExpress.ExpressApp.DC.PersistentAliasAttribute) and [XPO](xref:DevExpress.Xpo.PersistentAliasAttribute) support aliased/calculated properties that can be computed using SQL on the database server side for the best performance. This functionality has full support for XAF [Data Access Modes](xref:113683).
|-
| Backend Web API Service
| Both EF Core and XPO support [creation and modification of nested collections and reference properties](xref:403715#modify-an-object-assigned-to-a-reference-property) in our OData-powered Web API Service ([including OData Deep Update and Batch Operations](xref:405468))
|}

## XPO vs EF Core: Differences

{|
|-
! Aspect
! EF Core
! XPO
|-
| Product Type
| Free and [open-source](https://github.com/dotnet/efcore/blob/main/LICENSE.txt) product.

Maintained by Microsoft. 

EF Core source code is available on [GitHub](https://github.com/dotnet/efcore).
| The product is free, but proprietary. For more information, refer to the following page -- [EULA](https://www.devexpress.com/Support/EULAs/xpo.xml).

Maintained by DevExpress. 

XPO full source code is available to owners of DevExpress [Universal](https://www.devexpress.com/subscriptions/universal.xml) and [DXperience](https://www.devexpress.com/subscriptions/dxperience.xml) Subscriptions.
|-
| Status
| A mature ORM, heavily promoted by Microsoft, with active development on GitHub.

Product releases include annual major feature updates and monthly minor updates with bug fixes. 

| A mature ORM in maintenance mode. 

Annual major updates include support for new versions of .NET, Visual Studio, and the top 5 ADO.NET database drivers. Monthly minor updates contain bug fixes.
|-
| Popularity
| The [Microsoft.EntityFrameworkCore](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore) package has 2B total downloads with an average of 10M per day[^2]. 

It is easy to find and hire developers/contractors with EF knowledge.
| The [DevExpress.Xpo](https://www.nuget.org/packages/DevExpress.Xpo) NuGet package has 57M total downloads with an average of 375.3K per day[^2]. 

It is difficult to find and hire developers/contractors with XPO knowledge.
|-
| Community / Knowledge Base
| Entity Framework has over 135K public community-answered questions on Stack Overflow about the different ORM versions. Note that many solutions from older EF versions apply to more recent versions.

Comprehensive online documentation is available at [https://learn.microsoft.com/en-us/ef/](https://learn.microsoft.com/en-us/ef/). 

You can find thousands of third party educational resources for EF Core: community videos, tutorials, articles, and consulting/training materials.
| Stack Overflow contains less than 100 questions for XPO. The DevExpress Support Center lists about 16K public questions.

Comprehensive online documentation is available on the [DevExpress website](xref:1998). 

A limited number of third-party educational resources are available.
|-
| Database Provider Support
| [EF Core supports](https://learn.microsoft.com/en-us/ef/core/providers/) multiple popular relational database providers for .NET. 

Free and paid providers exist, both developed by Microsoft or third parties. You can also create custom database providers.

EF Core supports NoSQL databases (not currently used in XAF applications). 

Native support for spatial data, `DateTimeOffset`, and JSON types.
| [XPO supports](xref:2114) multiple popular relational database providers for .NET and the .NET Framework.

All existing providers are free and developed by DevExpress. You can create custom database providers. 

XPO does not support NoSQL databases. 

Create a custom solution to support spatial data, `DateTimeOffset` and JSON types.
|-
| Data Model Design
| EF Core has simple naming [conventions](https://learn.microsoft.com/en-us/ef/core/modeling/relationships/conventions) to define [relationships](https://learn.microsoft.com/en-us/ef/core/modeling/relationships), keys, and other property and entity types implicitly (without attributes) - see code examples in [](xref:402958). 

EF Core implicitly implements notifications when a property changes. Data model code allows virtual auto properties (`get;set;`) and does not require you to implement the `INotifyPropertyChanged` and `INotifyPropertyChanging` interfaces. For more information, refer to the following topic: [](xref:404292). 

You can also customize [the entity type structure or metadata using Fluent API](https://learn.microsoft.com/en-us/ef/core/modeling/) and [XAF Types info](xref:113583).
| XPO requires you to define [relationships](xref:2041) and [keys](xref:113665#xpo) explicitly (with attributes). 

XPO requires explicit notification when a property value changes. Data model code requires properties to include `SetPropertyValue` calls. For more information, refer to the following help section: [PropertyChanged Event in XPO](xref:117395#propertychanged-event-in-xpo). 

You can also customize the entity type structure or metadata using [XAF Types info](https://learn.microsoft.com/en-us/ef/core/modeling/) and [Model Editor](xref:113583#add-a-custom-calculated-field-in-the-model-editor)

|-
| Miscellaneous
| XAF does not support a nested `IObjectSpace` when EF Core is used as ORM. Each view has its independent Object Space. On the one hand, this offers a simpler UI and programming model. On the other hand, XPO may lack flexibility in certain advanced scenarios. XAF does not currently have an asynchronous `IObjectSpace` version for EF Core. 

EF Core does not allow you to add new properties to an existing data model dynamically (at runtime). 

| XPO allows you to [create a nested IObjectSpace](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.CreateNestedObjectSpace). When you commit changes in a nested Object Space, XPO merges them into the parent Object Space. This approach allows you to treat multiple related operations as a single operation. XAF also includes an asynchronous version of `IObjectSpace` for XPO. 

XPO allows you to add new properties to an existing data model dynamically through `XPDictionary` or [XAF Types info](xref:113583) (for advanced scenarios). 
|}



[^1]: EF Core supports Middle Tier Security in v23.1 and later.
[^2]: All statistics are current as of February 2026.
