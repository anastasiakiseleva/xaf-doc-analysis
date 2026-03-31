---
uid: "112559"
title: Plug-in MVC Architecture
seealso:
  - linkId: "113577"
  - linkType: HRef
    linkId: https://www.devexpress.com/products/net/application_framework/xaf-considerations-for-newcomers.xml
    altText: 'XAF Considerations for Newcomers'
---
# Plug-in MVC Architecture

Applications built with XAF consist of multiple functional blocks. The diagram below:
- Shows the basic blocks. 
- Indicates when and how these blocks are created.
- Shows you the areas where you can extend your applications. 

![Architecture](~/images/architecture116517.png)

This topic overviews each application building block.

## Storage
### ORM Layer

XAF works with data via an ORM Layer. With ORM, you have no need to create a database, configure tables, relations, and so on: ORM create a database for you. 

XAF supports the following ORMs:

- [XPO](https://www.devexpress.com/Products/NET/ORM/)
- [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/)

ORM tools allow you to use familiar code structures (classes, properties, and their attributes) to describe data for your application:
- To create a data table, declare a class. 
- Class' public properties define data fields in the data table. 
- The actual data set is a collection of class instances.
- To specify relations between tables, decorate classes and properties with specially designed attributes.

### Business Class Library

The [Business Class Library](xref:112571) implements the following:

* **Classes** that define frequently used entities like Person, Note, Organization, etc. You can review the source code of these classes for information on how to implement your data structures. Most customers implement their own business classes for production use. These built-in classes are mostly used for demo purposes.
* **Interfaces** that you may need to implement in your data classes. Some sub-systems of XAF require data to conform to particular rules. For instance, the security sub-system requires the **User** class to implement the [](xref:DevExpress.Persistent.Base.IPermissionPolicyUser) interface. If you develop your own class to represent application users, you have to [implement this interface](xref:113452#support-the-ipermissionpolicyuser-interface)

The image below shows some classes you can find in the **Business Class Library**.

![Business Objects Library](~/images/business-objects-library115257.png)

## User Interface (UI)

XAF separates business logic from the application's visual representation. XAF can create the following UIs based on the same business logic:

- A desktop WinForms application
- A web ASP.NET Core Blazor application

When you create a new application solution with XAF, a solution may include a web, desktop, or both projects. For more information about application solution components, refer to the following topic: [Application Solution Structure](xref:118045).

### Views

XAF automatically generates CRUD UI based on application data. 

**Example**. You have declared an ORM class that describes a person. This is all you need to get an application for storing contact information. You can start the application and it will display a person list using a grid control. You can add new entries or modify existing ones. These operations are performed using the automatically generated set of individual editors; each bound to a particular field.

The automatically generated UI elements used to display and manage data are called Views. In **XAF**, there are three types of Views.

List View
:   List Views are root modules of your application. Usually, these are grids that display collections that you work with (data tables). You see one of them when you start your project, and you can switch between them using the [Navigation System](xref:113198).  
![Architecture-ListViews](~/images/architecture-listviews115330.png)
Detail View
:   This View type deals with a single object (data record) and presents property values using standalone editors. You see these views when adding a new record or when modifying an existing one.
  ![Architecture-DetailViews](~/images/architecture-detailviews115329.png)
Dashboard View
:   This is a View that allows you to display multiple Views side-by-side on a single screen.  
![Architecture-DashboardViews](~/images/architecture-dashboardviews116734.png)

Views are built with the following DevExpress component suites:

- [Blazor](xref:400725) components.
- [WinForms](xref:7874) controls.

You can use any control you require to represent a List View or an editor within a Detail View. For information on Views and other elements that form a user interface, review documents from the [UI Construction](xref:112638) help section.

**See also**: [UI Customization Categories by Skill Level](https://www.devexpress.com/products/net/application_framework/xaf-considerations-for-newcomers.xml#ui-customization-categories)

### Additional Modules

You can extend XAF applications functionality with additional [modules](xref:118046) shipped with the **eXpressAppFramework**. A module is a ready-to-use feature that can be integrated to your XAF application. 

You can add the following modules to your XAF app:
- Modules shipped with XAF (Security, Reports, Dashboards, Office, Charts, Maps, etc.).
- Third-party modules (see [XAF Community Extensions](https://www.devexpress.com/products/net/application_framework/#extensions)).
- Your own custom [modules](xref:118046).

Refer to the following topics for details.

* [In-Depth Tutorial - Additional Modules](xref:403287)

## Behavior

### Built-in Controllers

Controllers are objects that manage your application flow. They are also responsible for end-user interaction. Even the simplest applications built with XAF use a number of [built-in Controllers](xref:113016) supplied with the **System Module** and [Additional Modules](xref:118046). These default Controllers are mostly responsible for data management. With their help, you can add new records, delete existing ones, perform full text search, and so on.

For the most part, Controllers serve as containers for **Actions**. Actions are abstractions of end-user interaction elements - buttons, menus, etc. An Action specifies the visual representation of a UI element and its associated code. So, you do not have to deal with low-level implementation details of particular editors, toolbar systems, context menus or anything else. At the same time, this higher-level of abstraction allows the same Action to be used in desktop and web applications.

For information on implementing your own Controllers and Actions, review the following documents:

* [Basic ASP.NET Core Blazor Tutorial](xref:401943) | [Define Custom Logic and UI Elements](xref:401954#define-custom-logic-and-ui-elements)
* [In-Depth Tutorial (Blazor and WinForms)](xref:402128) | **Add Actions (Menu Commands)** section
    
    This tutorial section shows you how to extend your application user interface with the help of Controllers. You will create Controllers with different Action types and Controllers without a single Action.
    
* [Controllers and Actions](xref:112623)
    
    This section explains how to use the Controllers-Actions technique in XAF to extend your applications with new features.

## Application Model

The **Application Model** stores all the information to build the XAF application UI.
For example, this information includes editor classes used for particular data types, or labels associated with particular fields.

The **Application Model** is automatically filled with metadata queried from application components - like business objects or Controllers.

XAF features the [Model Editor](xref:112582), which is integrated with **Microsoft Visual Studio**. You can use the **Model Editor** to edit the Application Model in both design time and runtime. To run it at design time, double-click a _.xafml_ file from any module or application project located in the **Solution Explorer**.

Application Model definition files are stored in XML format, you can edit them manually. 

For more information about the Application Model, refer to the following topics:

* [Basic ASP.NET Core Blazor Tutorial](xref:401943) | [Define Custom Logic and UI Elements](xref:401954#customize-the-application-ui-metadata)
* The **Customize the Application UI and Behavior** section in [In-Depth Tutorial (Blazor)](xref:402126)
    
    Lessons in this section of XAF tutorial demonstrate how you can use the Application Model to change the application user interface.
* [Application Model](xref:112579)
    
    This help section details how the Application Model is loaded, and how you can use it to customize the application user interface.
* [Application Migration to XAF](https://www.devexpress.com/products/net/application_framework/xaf-considerations-for-newcomers.xml#app-migration-to-xaf)
