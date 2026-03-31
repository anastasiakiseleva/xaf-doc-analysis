---
uid: "113683"
seealso:
- linkId: "118449"
- linkId: "118452"
- linkId: "118450"
- linkId: "113324"
title: List View Data Access Modes
---
# List View Data Access Modes

## Choose Data Access Mode
XAF uses the following default data access modes: 

* [Client](xref:118449): all XAF List Views, with the exception below. 
* [Queryable](xref:402925): ASP.NET Core Blazor Tree List Views and Lookup List Views. 

You can activate other modes to optimize how a List View loads and processes data:

* [Server](xref:118450), [InstantFeedback](xref:118450): a List View is bound to a large dataset.
* [DataView](xref:118452): objects that appear in a List View have a complicated structure (for example, include multiple reference properties).
* [ServerView](xref:118450), [InstantFeedbackView](xref:118450): large dataset and complicated object structure (both conditions above).

The following table explains these different modes:

{|
|-
! 
! [Client](xref:118449)
! [Queryable](xref:402925)
! [Server](xref:118450)
! [ServerView](xref:118450)
! [DataView](xref:118452)
! [InstantFeedback](xref:118450)
! [InstantFeedbackView](xref:118450)
|-

| **Platform**
| 
| 
| 
| 
| 
| 
| 
|-

| Blazor
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
|-

| WinForms
| ![supports](~/images/feature_suppoted.png)
| 
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
|-

| **ORM**
| 
| 
| 
| 
| 
| 
| 
|-

| EF Core
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
|-

| XPO
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
|-

| **Supported ListEditors**
| 
| 
| 
| 
| 
| 
| 
|-

| Blazor Grid
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
|-

| Blazor Lookup
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| 
| 
| 
| 
| 
|-

| Blazor Tree List
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| 
| 
| 
| 
| 
|-

| Blazor Chart
| ![supports](~/images/feature_suppoted.png)
| 
| 
| 
| ![supports](~/images/feature_suppoted.png)
| 
| 
|-

| Blazor Scheduler
| ![supports](~/images/feature_suppoted.png)
| 
| 
| 
| 
| 
| 
|-

| WinForms Grid
| ![supports](~/images/feature_suppoted.png)
| 
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
|-

| WinForms Tree List
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| 
| 
| 
| 
| 
|-

| WinForms Scheduler
| ![supports](~/images/feature_suppoted.png)
| 
| 
| 
| ![supports](~/images/feature_suppoted.png)
| 
| 
|-

| WinForms Pivot Grid
| ![supports](~/images/feature_suppoted.png)
| 
| 
| 
| ![supports](~/images/feature_suppoted.png)
| 
| 
|-

| **Processed Object**
| 
| 
| 
| 
| 
| 
| 
|-

| Original Object
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| 
| 
| 
| 
|-

| ObjectRecord
| 
| 
| 
| ![supports](~/images/feature_suppoted.png)
| 
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
|-

| XafDataViewRecord
| 
| 
| 
| 
| ![supports](~/images/feature_suppoted.png)
| 
| 
|-

| **Columns Available for Processing**
| 
| 
| 
| 
| 
| 
| 
|-

| Displayed Columns
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
|-

| Column from the Model
| ![supports](~/images/feature_suppoted.png)
| 
| ![supports](~/images/feature_suppoted.png)
| 
| 
| 
| 
|-

| Displayable Collection Properties
| 
| 
| 
| ![supports](~/images/feature_suppoted.png)
| 
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
|-

| **Initially Loaded Objects**
| 
| 
| 
| 
| 
| 
| 
|-

| All
| ![supports](~/images/feature_suppoted.png)
| 
| 
| 
| ![supports](~/images/feature_suppoted.png)
| 
| 
|-

| Displayed
| 
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| 
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
|-

| **Non-persistent Properties**
| 
| 
| 
| 
| 
| 
| 
|-

| Fully Supported
| ![supports](~/images/feature_suppoted.png)
| 
| 
| 
| 
| 
| 
|-

| Supported with Limitations
| 
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
|-

| **Additional Capabilities**
| 
| 
| 
| 
| 
| 
| 
|-

| Async Loading
| 
| 
| 
| 
| 
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
|-

| In-place Editing
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| ![supports](~/images/feature_suppoted.png)
| 
| 
| 
| 
|-


|}

For additional information about a specific data access mode, navigate to the corresponding help article. 

The following video explains the best ways to access and manipulate data in XAF, and how to build high-performance apps.

> [!video https://www.youtube.com/embed/RUyXX2pJcjM]

### Non-Persistent Properties: Support Limitations

Non-persistent properties return a value calculated at runtime or store a temporary value in memory. The following list describes their limitations in various data access modes:

* **ServerView**, **DataView**, **InstantFeedbackView**: List Editors do not display non-persistent property values. 
* **Server**, **InstantFeedback**, **Queryable**: List Editors display non-persistent properties but do not allow you to filter, sort, or group them.

To use non-persistent properties in these modes, decorate them with the [DevExpress.Xpo.PersistentAliasAttribute](xref:DevExpress.Xpo.PersistentAliasAttribute) (XPO) or [DevExpress.ExpressApp.DC.PersistentAliasAttribute](xref:DevExpress.ExpressApp.DC.PersistentAliasAttribute) (EF Core). For more information, refer to the following KB article: [Is it possible to avoid the "Cannot query a data store using criterion (…)" error and be able to filter, sort and group by non-persistent fields in server mode?](https://supportcenter.devexpress.com/ticket/details/q352044/server-and-instant-feedback-modes-sort-group-and-filter-by-non-persistent-fields-or-in).

## Specify Data Access Mode
To specify a List View's data access mode, invoke the [Model Editor](xref:112582), navigate to the [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] node, and set the [IModelListView.DataAccessMode](xref:DevExpress.ExpressApp.Model.IModelListView.DataAccessMode) property to the required [](xref:DevExpress.ExpressApp.CollectionSourceDataAccessMode) value.

![DataAccessMode](~/images/dataaccessmode117493.png)

[!include[DataAccessModeHelper.RegisterEditorSupportedModes Hint](~/templates/dataaccessmodehelper.registereditorsupportedmodes-hint111828.md)]

To change the data access mode for all List Views in an application (except for autogenerated nested List Views), invoke the Model Editor, navigate to the **Options** node, and specify its @DevExpress.ExpressApp.Model.IModelOptions.DataAccessMode property. To specify the data access mode for nested List Views, set the [IModelListView.DataAccessMode](xref:DevExpress.ExpressApp.Model.IModelListView.DataAccessMode) property for each nested List View node as described above.  

> [!note]
> * You can use [CollectionSource](xref:DevExpress.ExpressApp.CollectionSource.#ctor*) constructors with the _dataAccessMode_ parameter when you create a [List View's collection source](xref:DevExpress.ExpressApp.ListView.CollectionSource) in code.
> * [!include[server-based-data-access-modes-part-1-template](~/templates/server-based-data-access-modes-part-1-template.md)]
