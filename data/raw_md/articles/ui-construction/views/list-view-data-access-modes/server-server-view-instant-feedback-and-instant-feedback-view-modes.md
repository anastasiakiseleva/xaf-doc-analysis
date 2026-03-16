---
uid: "118450"
seealso:
- linkId: "8398"
title: Server, ServerView, InstantFeedback, and InstantFeedbackView Modes
owner: Ekaterina Kiseleva
---
# Server, ServerView, InstantFeedback, and InstantFeedbackView Modes

This article extends the [List View Data Access Modes](xref:113683) topic and details Server, ServerView, InstantFeedback, and InstantFeedbackView modes behavior.

## Notes on All Modes

* All these modes support XPO and EF Core ORMs.
* A [List View](xref:112611) does not have simultaneous access to all objects of the [ListView.CollectionSource](xref:DevExpress.ExpressApp.ListView.CollectionSource) type. Only those objects that are currently visible are loaded in small portions on demand. Each operation that assumes that new visible objects will appear (scrolling, paging, grouping, sorting) requires additional data requests.
* If you have a custom [Controller](xref:112621) that accesses the List Editor's control in a List View to execute custom sorting or grouping, the Controller may no longer work, since the database server executes grouping and sorting. Custom summaries are also calculated on the server side.
* In **ServerView**, **InstantFeedbackView**, and **DataView** modes, List Editors do not display [non-persistent property](xref:116516) values. To show them, apply the [DevExpress.Xpo.PersistentAliasAttribute](xref:DevExpress.Xpo.PersistentAliasAttribute) (XPO) or [DevExpress.ExpressApp.DC.PersistentAliasAttribute](xref:DevExpress.ExpressApp.DC.PersistentAliasAttribute) (EF Core) to these properties.
* List Editors do not support filter, sort, and group operations for non-persistent properties. To enable these operations, apply the [DevExpress.Xpo.PersistentAliasAttribute](xref:DevExpress.Xpo.PersistentAliasAttribute) (XPO) or [DevExpress.ExpressApp.DC.PersistentAliasAttribute](xref:DevExpress.ExpressApp.DC.PersistentAliasAttribute) (EF Core) to these properties.
* Inline editing is not supported in **ServerView**, **InstantFeedback**, and **InstantFeedbackView** modes. If an original object was modified, it is not displayed in a List View until you commit changes and reload the collection.
	
	For example, when an Action changes an object's property value, this object's instance is created by the separate database request and the property value's modification is not applied to the grid until you commit changes (or it occurs automatically if the [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges) property is set to **true**).

* Controls that support these modes do not have full access to underlying data and cannot initiate filter, sort, and group operations on the client side. These operations are delegated to the underlying ORM (EF Core or XPO), which constructs an appropriate SQL statement and sends a query to the SQL server to retrieve a small portion of data that should immediately be displayed to the user. You cannot filter, sort, or group data against non-persistent properties -- it is not possible to build a SQL query against a runtime value that exists on the client side only, and execute it on the database server side. Filter, group, and sort operations are disabled if a property is non-persistent.
* If you want one of these modes to display a nested List View, make sure that there is no logic for sorting, filtering or anything else in the getter of the underlying collection, and there are no subscribers to the collection's events. This logic and subscribers will not be taken into account, because a standalone server collection will be created instead of the original collection.
* [!include[DataSourcePropertyVsServerMode_Note](~/templates/datasourcepropertyvsservermode_note11161.md)]
* If you use a legacy database where a table has a primary compound key, such a table cannot be used to supply data in **Server**, **ServerView**, **InstantFeedback**, and **InstantFeedbackView** mode.
* The **OpenObjectController.OpenObject** Action is inactive in the **ServerView**, **InstantFeedback**, and **InstantFeedbackView** modes.

## Notes on Server and ServerView Modes

* The following built-in List Editors currently support the **Server** and **ServerView** modes: [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) (WinForms) and [](xref:DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor) (ASP.NET Core Blazor).
* The **Server** mode supports [in-place editing](xref:113249#in-place-editing) except [Batch Edit](xref:113249#in-place-editing-customization-the-inlineeditmode-property) in [](xref:DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor).
* In the **ServerView** mode, the [View.CurrentObject](xref:DevExpress.ExpressApp.View.CurrentObject) and [View.SelectedObjects](xref:DevExpress.ExpressApp.View.SelectedObjects) properties return @DevExpress.ExpressApp.ObjectRecord objects instead of original business objects. To get the real object, use the [IObjectSpace.GetObject](xref:DevExpress.ExpressApp.IObjectSpace.GetObject(System.Object)) method.
* Data-aware operations (grouping, sorting, and so on) are performed synchronously by the database server and significantly increase the List View's performance when working with many objects. In these modes, all properties are calculated when it is required (only the visible properties in the GridView and properties that are used in the Appearance, Security rules, and so on, are calculated).

> [!Tip]
> **ServerView** is the fastest synchronous data access mode.

## Notes on InstantFeedback and InstantFeedbackView Modes

* These modes are compatible with the WinForms [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) and Blazor [](xref:DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor). These editors are used in the default configuration.
* The [View.CurrentObject](xref:DevExpress.ExpressApp.View.CurrentObject) and [View.SelectedObjects](xref:DevExpress.ExpressApp.View.SelectedObjects) properties return @DevExpress.ExpressApp.ObjectRecord objects instead of original business objects. To get the real object, use the [IObjectSpace.GetObject](xref:DevExpress.ExpressApp.IObjectSpace.GetObject(System.Object)) method.
* Data-aware operations are performed asynchronously in a background thread, and the control continues to respond to the user's actions while data is being retrieved.
* In the **InstantFeedback** mode, you can implement custom logic in the @DevExpress.Xpo.IXPObject.OnLoading or @DevExpress.Persistent.BaseImpl.BaseObject.AfterConstruction method.
* In XPO, the [CollectionSourceBase.DisplayableProperties](xref:DevExpress.ExpressApp.CollectionSourceBase.DisplayableProperties) collection contains names of all visible properties and properties listed in [XPInstantFeedbackSource.DisplayableProperties](xref:DevExpress.Xpo.XPInstantFeedbackSource.DisplayableProperties). Properties that are hidden in the UI but are listed in **CollectionSourceBase.DisplayableProperties** may have complicated logic in getters, which require many database requests. This behavior may cause performance issues. You can change the default behavior using the [XPObjectSpace.InstantFeedbackMappingMode](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.InstantFeedbackMappingMode)  property.
* In EF Core, the [CollectionSourceBase.DisplayableProperties](xref:DevExpress.ExpressApp.CollectionSourceBase.DisplayableProperties) collection contains names of visible properties only.
* A List View makes additional database requests if an [Appearance](xref:113286)/[Security](xref:113366) rule or [PersistentAlias](xref:DevExpress.Xpo.PersistentAliasAttribute)/[Calculated](xref:DevExpress.ExpressApp.DC.CalculatedAttribute) attribute's expression uses properties that are not in the **CollectionSourceBase.DisplayableProperties** collection. To avoid excess requests, add these properties to **CollectionSourceBase.DisplayableProperties**. You can access all properties listed in this collection without additional requests.
* [Reference properties](xref:113572) are automatically replaced by default properties of the corresponding reference objects when sorting, grouping, and filtering. For instance, in the **Contact** List View, the **Contact.Department.Title** property is used instead of **Contact.Department**.
* If you use EF Core as your ORM system and **InstantFeedback** as the data access mode, you can implement cascade deletion of Aggregated collections as described in the **Cascade Deletion for Aggregated Entities** section of the [Relationships Between Entities in Code and UI](xref:402958) help topic.

> [!Tip]
> **InstantFeedbackView** is the fastest asynchronous data access mode.
