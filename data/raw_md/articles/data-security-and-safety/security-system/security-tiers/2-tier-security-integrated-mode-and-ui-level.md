---
uid: "113436"
seealso: []
title: 2-Tier Security (Integrated Mode and UI Level)
owner: Ekaterina Kiseleva
---
# 2-Tier Security (Integrated Mode and UI Level)

Applications with 2-Tier Security directly connect to the database (without the [Middle Tier Application Server](xref:113439)). This topic describes the following 2-Tier Security modes:

* [Integrated Mode](#integrated-mode-xpo-and-ef-core) (XPO and EF Core only)
* [UI-Level Mode](#ui-level-mode)

> [!NOTE]
> [!include[BypassClientSideSecurity](~/templates/BypassClientSideSecurity.md)]
> 
> Use a Middle Tier application server between your application and the database server instead of client-side security. The following help topic describes how to set it up: [Middle Tier Security](xref:113439).

## Integrated Mode (XPO and EF Core)

@DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider (XPO) / @DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1 (EF Core) creates secured Object Spaces that incorporate [security permissions](xref:113366) and filter protected data at the ORM level. As a result, secured data is not displayed in [Views](xref:112611) and [Controllers](xref:112621) or [report data sources](xref:113593) cannot access the data.

The following sections describe how applications with Integrated Security interacts with the database:

### XPO-Based Applications

> [!ImageGallery]
> ![XPO-based application with the Integrated Security](~/images/ApplicationWithIntegratedSecurity_diagram.png)
> ![Application without the Security System](~/images/NonSecureApplication_diagram.png)

#### Load Data from the Database 
1. The unsecure `Session` loads from the database objects that meet the criteria generated according to [Security permissions](xref:113366).
2. The secured `Session` copies objects from the unsecure `Session`. If a field value does not meet the permission criterion, it is replaced with the default value in the copied objects. Copied objects are available to users.

#### Save Data to the Database
1. The secured `Session` copies object values that meet the Security permissions to the unsecure `Session`.
2. The unsecure `Session` saves the passed values in original objects in the database.

### EF Core-Based Applications

> [!ImageGallery]
> ![EF Core-based application with the Integrated Security](~/images/ApplicationWithIntegratedSecurityEFCore_diagram.png)
> ![Application without the Security System](~/images/NonSecureApplication_diagram.png)

#### Load Data from the Database
1. The internal Security service that extends `DbContext` loads from the database objects that meet the criteria generated according to [Security permissions](xref:113366). This service copies the loaded objects and replaces the original property value with the default value if this property does not meet the permission criterion.
2. The internal Security service passes copied objects to the Secured Object Space. These objects are available to users.

#### Save Data to the Database 
1. The secured Object Space passes object values to the internal Security service that extends `DbContext`.
2. The internal Security service saves the passed values that meet the Security permissions into the database.
### Important Notes

[!include[SecuredApplications-ImportantNotes](~/templates/SecuredApplications-ImportantNotes.md)]

* To bypass security, call the `CreateNonsecuredObjectSpace` ([XPO](xref:DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider.CreateNonsecuredObjectSpace)/[EF Core](xref:DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1.CreateNonsecuredObjectSpace)) to create an unsecured @DevExpress.ExpressApp.IObjectSpace instance. Then, use this Object Space's methods and access protected data as described in the following help topic: [Create, Read, Update and Delete Data](xref:113711).
    > [!Note]
    > You cannot create a non-secured Object Space on the client side if you use Middle Tier Security Server. To specify an object property's value bypassing the security system, use the [SetPropertyValueWithSecurityBypass](xref:DevExpress.ExpressApp.Xpo.SecuredPropertySetter.SetPropertyValueWithSecurityBypass``1(System.Object,System.String,``0)) method.

## UI Level Mode

We do not recommend that you use this mode in XPO-based and EF Core-based applications because applications have direct access to the database in this mode, and you can modify protected data in code (for example, in Controllers). List and Property Editors hide the protected data on the UI level only.

![Application with the UI-Level Security System](~/images/NonSecureApplication_diagram.png)

### Important Notes

* List Editors sort, filter, and group data values, but display placeholder text ('\*\*\*\*\*\*\*') instead of protected values.
* Web page markup contains real values.
* The appearance of a View that displays an object may change after a user modifies this object property. For example, the object has the `Name` property and object-level permission denies writing objects with criteria `Name = Example`. In this case, this object is displayed as read-only after the user saves it if the user creates an object and sets its `Name` property to `Example`.
* [Additional Modules](xref:118046) do not take into account Security permissions. They have direct access to the database through unsecured Object Spaces and can use protected records.
