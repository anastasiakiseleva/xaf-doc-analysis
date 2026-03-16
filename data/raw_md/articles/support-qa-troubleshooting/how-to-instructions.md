---
uid: "113054"
title: '"How-to" Instructions'
---
# "How-to" Instructions

Below is a list of topics answering the most frequently asked questions about XAF.

[How to: Implement Cascading Filtering for Lookup List Views](xref:112681)
:   Illustrates how to set up Lookup Property Editor filtering in the [Application Model](xref:112580) and programmatically, and describes multiple scenarios.
[How to: Get the Current User in Code](xref:113152)
:   Specifies how to work with the static [](xref:DevExpress.ExpressApp.SecuritySystem) class's properties to access the user name, user ID or the entire user object. It also describes granting access only to objects the current user owns.
[How to: Use Custom Logon Parameters and Authentication](xref:404264)
:   Describes how to replace the "User Name" editor displayed in the logon dialog with two Lookup Property Editors: the first one for choosing a company, the second one for choosing an employee from this company.
[How to: Calculate a Property Value Based on Values from a Detail Collection](xref:113179)
:   Explains how to implement a business class, so that one of its properties is calculated based on a property(s) of the objects contained in the child object collection.
[How to: Initialize Business Objects with Default Property Values in XPO](xref:113258) and [How to: Initialize Business Objects with Default Property Values in Entity Framework Core](xref:402990)
:   Describes how to initialize different types of properties with default property values.
[How to: Implement Custom Security Objects (Users, Roles, Operation Permissions)](xref:113384)
:   Illustrates how to create custom security objects, such as permissions, roles, and users, as well as implement an export functionality using a custom CanExport property.
[How to: Access Objects Selected in the Current View](xref:113324)
:   Explains how to manipulate focused and selected objects by accessing them from [Controllers](xref:112621) and [Actions](xref:112622) and modifying their properties - provides sample code snippets.
[How to: Generate XPO Business Classes for Existing Data Tables](xref:113451)
:   Describes how to set up your XAF application to work with existing databases by generating a business model declaration for the specified legacy database and mapping existing tables to persistent objects.
[How to: Include an Action to a Detail View Layout](xref:112816)
:   Uses an Action Container View Item to make an [Action](xref:112622) available in a View (Detail View or Dashboard View) and not a toolbar.
[How to: Display a List of Non-Persistent Objects in a Popup Dialog](xref:113167)
:   Populates and displays a list of objects that are not bound to the database ([Non-Persistent Objects](xref:116516)).
[How to: Change an Application Logo and Info](xref:113156)
:   Illustrates how to change the default logo image and text displayed in the application's About section.
[How to: Implement a Custom Security System User Based on an Existing Business Class](xref:113452)
:   Merges a business class with the Security System's User object so that the Security System would recognize the business class's objects as possible User types.
Contains information on hiding secure data for EF Core applications.
[How to: Print a Report Without Displaying a Preview](xref:113601)
:   Explains how to implement an Action in WinForms and ASP.NET Web Forms applications that prints a report without displaying its preview.
[How to: Specify a Display Member (for a Lookup Editor, Detail Form Caption, etc.)](xref:113525)
:   Describes how to configure a business object to display a specific property's value in Lookup Editors, Detail Form captions, etc., by default.
	Specify a business object’s property
[How to: Display a Non-Persistent Object's Detail View from the Navigation](xref:113471)
:   Specifies how to display a [non-persistent objects](xref:116516)' Detail View in the Navigation or as a Dashboard item.
[How to: Display a Non-Persistent Object's List View from the Navigation](xref:114052)
:   Displays a [non-persistent objects](xref:116516)' List View in the Navigation.
[How to: Show a Custom Data-Bound Control in an XAF View (WinForms)](xref:114159)
:   Adds a custom data-bound (data-aware) control to a View and display this View in a WinForms or ASP.NET Web Forms XAF application's navigation.
[How to: Create an Action Using the Action Attribute](xref:112619)
:   Illustrates how to create an [Action](xref:112622) within a persistent class declaration (that is, how to convert a persistent class method into a [](xref:DevExpress.ExpressApp.Actions.SimpleAction) or [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction)).
[How to: Create a Custom WinForms Ribbon Template](xref:112618)
:   Explains how to modify the default Ribbon template (XAF provides two default templates - Ribbon and Standard), create a ribbon page group and add an [Action](xref:112622) to it.
[How to: Deactivate (Hide) an Action in Code](xref:112728)
:   Deactivates predefined or custom [Actions](xref:112622) and explains how the [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) property controls the Action's visibility.
[How to: Disable and Hide Property Editors Based on a Business Rule](xref:113221)
:   Offers step-by-step instructions on using the [Conditional Appearance Module](xref:113286) to disable/enable and show/hide Property Editors based on business rules.
[How to: Implement a Property Editor Based on a Custom Control (WinForms)](xref:112679)
:   Explains how to implement a Property Editor in WinForms applications.
[How to: Map a Persistent Class to a Database View Which Has No Key Field](xref:113281)
:   Illustrates how to access stored queries in a database, which has no key field, by implementing a persistent class mapped to that database view.
[How to: Access the Master Object from a Nested List View](xref:113161)
:   Describes how to access a master object. This may be necessary when you have a [Controller](xref:112621) for a nested List View displaying an object collection.
[How to: Create a Business Model in the XPO Data Model Designer](xref:113450)
:   Gives step-by-step instructions on using the XPO Data Model Designer in XAF applications. The topic covers creating a simple business model of two objects linked with a one-to-many relationship and adding XAF-specific attributes in code.
[How to: Initialize an Object Created Using the New Action](xref:112912)
:   Initializes a property of an object created using the New Action.
[How to: Customize Action Controls](xref:113183)
:   Describes how to customize the control that visualizes an Action in a UI. The topic covers creating a custom [Action](xref:112622) and modifying it to accept keyboard input using a custom mask.