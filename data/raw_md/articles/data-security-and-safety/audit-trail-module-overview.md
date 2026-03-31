---
uid: "112782"
title: Audit Trail (History of Data Changes)
---
# Audit Trail (History of Data Changes)

The Audit Trail Module logs information on changes made to the persistent objects and stores this information in the application database. You can retrieve information on a specific change type (for example, object creation or update), the author of this change, the modified object, and the previous and new property values. 

Windows Forms
:   ![The Audit Trail System in the WinForms application](~/images/AuditTrail_Gallery_Win.png)
ASP.NET Core Blazor
:   ![The Audit Trail System in the ASP.NET Core Blazor application](~/images/AuditTrail_Gallery_Blazor.png)

## Audit Trail System Components

The Audit Trail System includes two ORM-specific modules:

* [Audit Trail Module for XPO-based WinForms and ASP.NET Core Blazor applications](xref:403114)
* [Audit Trail Module for EF Core-based WinForms and ASP.NET Core Blazor applications](xref:403104)

These topics describe how to add the Module to your application and explain ORM-specific behavior.

You can also use the Audit Trail Module in non-XAF applications. For more information, refer to the following example: [Audit Trail: Log Data Changes Made via Web API Endpoints](xref:404262)

## Tracked Changes

The following table lists all changes that the Audit Trail Module logs:

| Change | Description |
|---|---|
| ObjectCreated | The audited object is created. |
| InitialValueAssigned | An initial value is assigned to the audited object before the first save. |
| ObjectChanged | The audited object property is changed. |
| ObjectDeleted | The audited object is deleted. |
| AddedToCollection | The audited object is added to a collection. |
| RemovedFromCollection | The audited object is removed from a collection. |
| CollectionObjectChanged | An object from the audited object is changed. |
| AggregatedObjectChanged (XPO only) | An object aggregated with the audited object is changed. |
| CustomData | Custom data is added to the audit log. |

## Important Notes 

* The Audit Trail Module logs operations made inside an application only. It does not store the information on modifications made in the database (for example, cascade deletion).
* This Module manages numerous audited changes in one transaction. This may take significant time to save audit data records and cause performance issues. We recommend that you investigate if this behavior suits your scenario before you use this Module in your application.
