---
uid: "112925"
seealso: []
title: 'How to: Add a Search Action to Lookup Property Editors and Link Pop-up Windows'
---
# How to: Add a Search Action to Lookup Property Editors and Link Pop-up Windows

Lookup Property Editors that display reference properties contain a list of existing objects of the specified type in the drop-down menu. Similarly, the Link Action's pop-up windows display a list of available objects of the specified type. The following image demonstrates both the Lookup Property Editor's drop-down window and the Link Action's pop-up window:

ASP.NET Core Blazor
:   ![XAF ASP.NET Core Blazor Lookup Property Editor and Link Popup Window, DevExpress](~/images/xaf-blazor-lookup-property-editor-link-popup-window-devexpress.png)
Windows Forms
:   ![XAF Windows Forms Lookup Property Editor and Link Popup Window, DevExpress](~/images/howtoaddsearchfunctionality116020.png)

This topic explains how to enable the Search functionality that allows you to quickly find the required object when there are many objects to be shown.

> [!NOTE]
> In XAF ASP.NET Core Blazor applications, the Search functionality is always available in the Link Action's pop-up window.

## Search Functionality

ASP.NET Core Blazor
:   ![|XAF ASP.NET Core Blazor Look-up Property Editor in Search Mode, DevExpress](~/images/xaf-blazor-lookup-property-editor-search-mode-devexpress.png)

    ![|XAF ASP.NET Core Blazor Look-up Property Editor Search Pop-up Window, DevExpress](~/images/xaf-blazor-lookup-property-editor-popup-search-window-devexpress.png)
Windows Forms
:   ![XAF Windows Forms Look-up Property Editor in Search Mode, DevExpress](~/images/searchinlookup116022.png)

The **Search** button executes [FullTextFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextFilterAction) of the [](xref:DevExpress.ExpressApp.SystemModule.FilterController). It looks for objects where property values (string representations) include the value specified by the user. Properties that take part in search are listed in the [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] node that defines the List View. They can be visible or hidden, persistent or non-persistent. For more information, refer to the following topic: [](xref:DevExpress.ExpressApp.SystemModule.FilterController).

## Automatic Activation

In Windows Forms applications, XAF automatically enables the Search functionality when a List View in a Lookup Property Editor or Link Action's pop-up window contains more than 25 objects.

You can specify a different limit in the [IModelOptions.LookupSmallCollectionItemCount](xref:DevExpress.ExpressApp.Model.IModelOptions.LookupSmallCollectionItemCount) property of the [Application Model](xref:112580)'s **Options** node.

![|XAF LookupSmallCollectionItemCount Property in Model Editor, DevExpress](~/images/lookupsmallcollectionitemcount119000.png)

## In Code

To enable the Search functionality in the Lookup Property Editor or Link Action's pop-up window with any number of objects in the List View's collection source, apply the [](xref:DevExpress.Persistent.Base.LookupEditorModeAttribute) to the required property (a reference of collection property). Specify one of the following modes for the corresponding Lookup Property Editor or Link Action's pop-up window:

{|
|-

! Mode
! Loaded objects
! Search functionality
|-
| `Auto`
| **ASP.NET Core Blazor:** All objects of the specified type.

**Windows Forms:** None if the object count in the property's data source collection is less than the value of the @DevExpress.ExpressApp.Model.IModelOptions.LookupSmallCollectionItemCount property.
| **ASP.NET Core Blazor:** Disabled. Only native @DevExpress.Blazor.DxComboBox`2 search is available.

**Windows Forms:** Disabled if the object count in the property's data source collection is less than the value of the @DevExpress.ExpressApp.Model.IModelOptions.LookupSmallCollectionItemCount property.
|-
|  `AllItems`
| All objects of the specified type.
| Only native @DevExpress.Blazor.DxComboBox`2 search is available.
|-
| `Search`
| None.
| Enabled.
|-
| `AllItemsWithSearch`
| All objects of the specified type.
| Enabled.
|}

To set the required mode, pass the corresponding value as the `LookupEditorModeAttribute`'s parameter.

## In Application Model

In the [Model Editor](xref:112582), set the **LookupEditorMode** property of the **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node to the required value.
