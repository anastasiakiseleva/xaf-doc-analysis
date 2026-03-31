---
uid: "112558"
title: Comparison With Other Methodologies
---
# Comparison With Other Methodologies

Companies store and manage a lot of information about employees, clients, sales, etc. They also keep track of their operations and automate their workflow. Every company needs software for daily operations, and the quality of this software is crucial to the success of their business. Imagine a restaurant that allows you to reserve a table online, or a bank that allows you to get a credit card activity report summarized and grouped in any manner you like. Such service enhancements create happier customers and stronger sales.

A company can either get the required software from one of the two traditional sources we have or it can move forward with the help of XAF. Take a look at the pros and cons for each of these methods of producing software.

## Scenario #1 - Create Software from Scratch
A company can either order software written from scratch from an independent software company or from the company's IT department, if one exists. If programmers are not relying on a framework that facilitates business application development, they will face the following problems.

* Lots of time will be expended producing even the simplest applications for storing and viewing information. Developers will have to tend to every single aspect of that application - from manual data management in a DBMS, to providing editors for each and every field they require to be edited.
* Extensive time and resources will be needed for testing purposes. All software has bugs, so inevitably, an application written from scratch will have many bugs. The only way to avoid them in the first stages of application development is to re-use software pieces that have already been well tested. Of course, developers will try to re-use as much of their own code as possible, but nevertheless, the amount of re-used code will most likely be very small in comparison to the entire application.
* It is difficult to maintain and extend such applications. The abstraction level is quite low - developers are responsible for every control on every form. So, even for a small task, like adjusting an editor for a particular data type, they will have to open numerous forms and manually customize them. This can lead to possible errors. The more complex an application is, the more difficult it gets.

Of course, this scenario also has its advantages.

* Every single aspect of an application will be under the total control of its developers. The only external thing developers cannot change is development tools. Everything else is created by them, known by them and presumably will be more easily maintained and fixed by them.
* Developers can optimize the software for the needs of this particular application, which is impossible when a universal software product or library is used.
* Applications do not have to follow the rules of some external system. The more help such a system offers, the more specific tasks can be accomplished in concert with the external system.

If you are not building similar applications each and every time, but rather creating unique, individual applications , then creating applications from scratch is the best choice.

## Scenario #2 - Adopt a Universal Software Product
A business could buy a product like [Microsoft Dynamics AX](https://en.wikipedia.org/wiki/Microsoft_Dynamics_AX), and hire consultants to configure it as required. This approach has the following disadvantages.

* It demands learning a special programming language, which can prove costly.
* It does not allow customizing and extending applications.
* Typically, universal products lack in performance.

The pros are:

* If you adopt a well-known system, you can be fairly well assured that it has already been well tested, and you will not experience problems with quality.
* In this case, a business does not have to deal with programming professionals.

This scenario is best if something common and simple is needed;  if no innovations are planned, and there is no need to have software that is unique in their business class.

## Scenario #3 - Use XAF
XAF lies somewhere between the two scenarios described above. Developers still need to write code, but a great deal of it has already been completed for them. XAF gives them a development platform that makes it much easier to develop business applications. These are the applications described at the beginning of this overview - those designed to enter, store, browse, analyze, print data, or if needed, organize company workflow. If you are trying to build an application of another type - a game, a graphic editor, a word processor, and so on. - XAF will not help you.

There are a number of things that you have to create each time you develop a business application - these elements are quite similar, and yet there's no easy way to re-use code. You have to setup datasets, grids, entry forms, etc. But, instead of doing this routine work, XAF offers you a high level interface hiding these implementation details, and letting you concentrate on business logic. For example, with XAF, it is much easier to declare and access data than using ADO.NET, and you have to do little work to create a UI for data management.

Of course, XAF was initially designed to address issues that take place when you develop an application from scratch. Thus, the main goals of XAF technology are:

* Easily re-use the same business logic in applications designed for different platforms (WinForms and ASP.NET Core Blazor).
* Provide data-to-UI construction algorithms. This means that you do not need to manually create many similar forms for data browsing and editing. This also makes it easy to maintain applications, since if you change data, you do not have to modify numerous forms and/or web pages - it is done automatically.
* Hide data management details. You will not have to deal with any DBMS or use ADO.NET to access data. XAF gives you a higher-level tool for data management. This tool makes it easy to store your data using any popular DBMS, without having to be familiar with it in detail. It is also easy to change the target database management system.
* Makes it extremely easy to create business applications designed to store and view data.
* Allows applications to be created using any .NET language.

There are more features that make XAF the best option.

* It is easily extensible. You can customize or fully replace almost every built-in application UI element or standard behavior. You can also combine traditional development approaches (e.g., show existing custom forms or controls) with pure XAF approaches, if required. Finally, XAF comes with the full source code which you are free to modify, though it is practically unnecessary due to its great flexibility and extensibility. This all makes the [vendor lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in) effect impossible with XAF.
* The quality of major constituent parts is guaranteed. The [XPO ORM](https://www.devexpress.com/products/net/orm/) or [Entity Framework (EF) Core](https://learn.microsoft.com/en-us/ef/core/) used as the [object-relational mapping](https://en.wikipedia.org/wiki/Object-relational_mapping) tool and visual components from the [DXperience Subscription](https://www.devexpress.com/Subscriptions/DXperience.xml) are all leading products of their kind. So, they are well-tested and highly reliable.

## Learn more about XAF
Refer to the following sections for more information about XAF.

* [XAF Architecture](xref:112559)

	Describes the main concepts that you need to know to use XAF.

* [Considerations for Newcomers](https://www.devexpress.com/products/net/application_framework/xaf-considerations-for-newcomers.xml)

    This article documents some of XAF's capabilities, and describes the experience/knowledge level required to maximize its potential.

* [Getting Started Tutorials and Videos](xref:113577)

	Follow these walkthrough tutorials or watch our introduction videos to create your first applications using XAF.

* [!include[Roadmap_Link](~/templates/Roadmap_Link.md)]
