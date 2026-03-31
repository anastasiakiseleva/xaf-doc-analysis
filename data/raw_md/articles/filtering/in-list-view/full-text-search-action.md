---
uid: "112997"
seealso: []
title: FullTextSearch Action
---
# FullTextSearch Action

Use this Action to filter the current List View.

When you type a word combination in the Action's text box, the List View displays only objects whose property values contain individual words from this combination. When you clear the text box, the List View displays all objects.

ASP.NET Core Blazor
:   ![|FullTextSearch Action in ASP.NET Core Blazor, DevExpress|](~/images/filters_blazor.png)
Windows Forms
:   ![|FullTextSearch Action in Windows Forms, DevExpress|](~/images/filters_win_1115953.png)

The **FullTextSearch** Action belongs to the [](xref:DevExpress.ExpressApp.SystemModule.FilterController). To access the Action in code, use the [FilterController.FullTextFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextFilterAction) property.

For instructions on how to customize the **FullTextSearch** Action's search engine, refer to the following topics:

* [FilterController.FullTextFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextFilterAction).
* [How to: Make the FullTextSearch Action Search Within Required Properties](xref:112923).

## FullTextSearch Action in a Lookup Property's or Link Action's Window

The **FullTextSearch** Action is available in the Lookup Property Editor's drop-down window or the **Link** Action's pop-up window.

In Windows Forms applications, XAF enables the Action automatically, if the count of the objects in the List View is more than the value specified for the [IModelOptions.LookupSmallCollectionItemCount](xref:DevExpress.ExpressApp.Model.IModelOptions.LookupSmallCollectionItemCount) property of the [Application Model](xref:112580)'s **Options** node.

In ASP.NET Core Blazor applications, the **FullTextSearch** Action is enabled automatically in the **Link** Action's pop-up window. To learn how to enable the **FullTextSearch** Action in Lookup Property Editors, refer to the following topic: [How to: Add a Search Action to Lookup Property Editors and Link Pop-up Windows](xref:112925).
