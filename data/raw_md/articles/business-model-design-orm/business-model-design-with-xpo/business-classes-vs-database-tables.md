---
uid: "112570"
seealso:
- linkId: 2537
- linkId: "113325"
- linkId: "112847"
title: Business Classes vs Database Tables
---
# Business Classes vs Database Tables

The **XAF** is based on an object-based data handling approach. In this topic, we discuss the reasons why this approach, as opposed to the relational model of data handling, was chosen. The methods that allow utilization of this approach are also defined in this document.

In an application where you have to deal with information, you most likely have database tables, database systems, SQL queries, records and columns. Using relational models is a traditional way to work with databases. Today, the most common approach to database access is probably ADO.NET technology. It has the DataSet type that grants a local copy of multiple interrelated database tables. Via the DataSet object, a user can locally execute various operations, with the content of a database being physically disconnected from the DBMS.

The **XAF** concentrates its efforts on another flow of today's development: object-oriented data handling. The need to store object-oriented data appeared when object-oriented programming became pervasive. Currently, most modern, nontrivial applications use an object-oriented paradigm to model application domains. This means that you can abstract from any persistence details, and have a clean, simple, object-oriented API to perform data storage. You do not need to handle persistence details and internal data representation in data stores be they relational, object-based, or something else. Why should you deal with low-level constructs of the data-store model, such as rows and columns, and constantly translate them back and forth? Instead, concentrate on complex applications you are required to deliver.

The ability to use object-based data handling, instead of direct interaction with databases, leads to a layer that provides mapping of objects into database tables (Object-Relational Mapping tool). In the **XAF**, such a layer is provided by the [XPO ORM](https://www.devexpress.com/Products/NET/ORM/). The **XPO** provides reliability and flexibility in storing the information, proven by years as a standalone product. Its simplicity comes from the fact that you do not need to learn the details of how the data is stored.

With the **XPO** layer, to persist a class (to provide its mapping) all that you need to do is to inherit it from the [](xref:DevExpress.Xpo.XPObject) class. This class has the [XPObject.Oid](xref:DevExpress.Xpo.XPObject.Oid) property that uniquely specifies an object. In the **XAF**, the [](xref:DevExpress.Persistent.BaseImpl.BaseObject) class is used as a persistent class. It is inherited from the [](xref:DevExpress.Xpo.XPCustomObject) class to satisfy the Framework's needs. **XPO** reads the content of a persistent class, and creates a database table for its read-write public fields and properties. By default, **XPO** gives the database table the same name as the class, and stores data in fields with the same name as the properties. You can easily override this behavior by using the [](xref:DevExpress.Xpo.PersistentAttribute). The **Persistent** attribute can also be used to make **XPO** persist a private field, if required. If there is a property, class or field that you do not want to persist for any reason (for instance, a property's value is calculated in code), use the [](xref:DevExpress.Xpo.NonPersistentAttribute). For more information on **XPO**, refer to the [XPO Online Documentation](xref:1998).

[!include[](~/templates/baseobject_codesnippet.md)]

Applying the **DefaultClassOptions** (see [](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute)) attribute to a class creates the following capabilities:

* The Contact item is added to the main form's navigation control. When clicking this item, a list of the objects of the Contact type will be displayed.
* The Contact item is added to the submenu of the **New** toolbar button when objects of another type are displayed. Click this item to invoke a Contact detail form and create a new Contact object.
* The Contact objects is provided as a data source to generate reports (see [](xref:404206)).
* The Contact item is added to the types list in the **Dashboards Data Source Wizard**. This allows end-users to create [dashboards](xref:117449) for objects of this class (see [Create, View and Modify Dashboards in a WinForms Application](xref:117450)).

To apply each of these options separately, use the **NavigationItem**, **CreateableItem**, **VisibleInReports** and **VisibleInDashboards** attributes, respectively (see [](xref:DevExpress.Persistent.Base.NavigationItemAttribute), [](xref:DevExpress.Persistent.Base.CreatableItemAttribute), [](xref:DevExpress.Persistent.Base.VisibleInReportsAttribute) and [](xref:DevExpress.Persistent.Base.VisibleInDashboardsAttribute)).

Using the **SetPropertyValue** is required by XPO. For details, refer to the [Creating a Persistent Object](xref:2077) topic.

When running the application for the first time, a database is created, and tables for all persistent classes found are created. The following image shows the Contact table corresponding to the Contact class defined above:

> [!NOTE]
> [CodeRush](https://www.devexpress.com/products/coderush/) includes a number of Code Templates that help generate business classes or their parts with a few keystrokes. To learn about the Code Templates for **XPO**, refer to the following help topic: [XPO and XAF Templates](xref:118557).

![ContactTable](~/images/contacttable115290.png)

Then, you can modify the implemented persistent classes, and add new ones. The database will be changed respectively, when running the application.

> [!NOTE]
> While XAF can create database schema objects, it cannot modify them later. For instance, column type and size cannot be changed automatically when you update your business class code.

A Contact object can be created by an end-user. The following picture demonstrates a populated Contact Detail View (the View is generated automatically, although you can [customize](xref:112611) it):

![Contact_DetailView](~/images/contact_detailview115291.png)

After saving changes in the Contact Detail View, the created object is mapped to the database. The following image demonstrates the Contact table with the record inserted:

![ContactTableWithRecord](~/images/contacttablewithrecord115289.png)

A new persistent object can be created and saved to the database in code. For details, refer to the [Supply Initial Data](xref:402985) topic. Generally, all operations on persistent objects are supposed to be performed via an [Object Space](xref:113707).

> [!NOTE]
> **XAF** does not use or initialize the **DevExpress.Xpo.XpoDefault** settings storage. So, the **XpoDefault.Session** or **Session.DefaultSession** Sessions should not be used in **XAF** applications. If you need to access a valid Session that uses the correct connection string, you have the following options:
> 
> * In the context of a Business Class - use the **Session** property, available in all the persistent types that inherit from the **DevExpress.Xpo.PersistentBase** class.
> * In the context of a [Controller](xref:112621) - you can access the [](xref:DevExpress.ExpressApp.XafApplication) object via the [Controller.Application](xref:DevExpress.ExpressApp.Controller.Application) property. The **XafApplication** object, in turn, has the [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) method. You can use this method to create a new Object Space and access its Session via the [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session) property.

As you see, you do not need to be concerned with a database, its tables and record queries. You deal only with classes and their properties.

You can set relationships between database tables by defining relationships between objects. Refer to the following link for details: [Relationships Between Objects](xref:2041). The "One-to-Many" and "Many-to-Many" relationship types are defined via the [](xref:DevExpress.Xpo.AssociationAttribute). The "Many" relationship part is represented by the [](xref:DevExpress.Xpo.XPCollection) type property.

The **XAF** not only spares you the difficulties of direct contact with database tables, it also allows you to use the ready-to-use business classes. The **XAF** has the Business Class Library - a collection of classes that describe entities frequently used in business applications - personal information, addresses, etc. This means that you do not have to build your data structure from scratch - we have already implemented the most frequently used templates for you. You may only need to extend them with custom attributes, and create appropriate relations. For details on the Business Class Library, refer to the [Built-in Business Classes for Most Popular Scenarios](xref:112571) topic.

If you have a large database and want to use it in an XAF application, refer to the [How to: Generate XPO Business Classes for Existing Data Tables](xref:113451) topic.
