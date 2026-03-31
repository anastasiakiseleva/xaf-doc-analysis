---
uid: '401747'
title: Asynchronous Data Loading (Windows Forms)
seealso:
  - linkId: '401750'
---
# Asynchronous Data Loading (Windows Forms)

This article describes how to load View data asynchronously in WinForms applications. This capability allows you to keep the UI responsive while the application fetches required data. End users can navigate to another View while the operation is in progress. They can also close the tab before the View loads all data, which would then cancel the data load operation.

![Asynchronous Data Loading](~/images/UseAsyncLoading_Runtime.png)

## Prerequisites

You should use @DevExpress.Xpo.ThreadSafeDataLayer in your application to enable asynchronous data loading. To use this data layer, follow the steps below:
1. Open the _Startup.cs_ file and locate the @DevExpress.ExpressApp.ApplicationBuilder.XPObjectSpaceProviderBuilderExtensions.AddXpo* method. 
2. Set the @DevExpress.ExpressApp.ApplicationBuilder.XPObjectSpaceProviderOptions.ThreadSafe option to `true`.

# [YourSolutionName.Win\Startup.cs](#tab/tabid-csharp)

```csharp
builder.ObjectSpaceProviders
    .AddXpo((application, options) => {
        options.ConnectionString = connectionString;
        options.ThreadSafe = true;
    })
    // ...
```
***

You can enable this feature for Views that fit all the conditions below.

{|
|-
! List View
! Detail View
|-

| * [IModelListView.EditorType](xref:DevExpress.ExpressApp.Model.IModelListView.EditorType) = @DevExpress.ExpressApp.Win.Editors.GridListEditor,<br/>@DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor, or @DevExpress.ExpressApp.Chart.Win.ChartListEditor
* [IModelListView.DataAccessMode](xref:DevExpress.ExpressApp.Model.IModelListView.DataAccessMode) = [Client](xref:118449)
* [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot) = `true`
* displays persistent objects
| * [DetailView.UseAsyncLoading](xref:DevExpress.ExpressApp.DetailView.UseAsyncLoading) = `true`
* [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot) = `true`
* displays a persistent object
|}

## Enable Asynchronous Loading

Set the @DevExpress.ExpressApp.Model.IModelAsync.UseAsyncLoading property to `true`. The following Model Editor nodes allow you to specify this property for supported Views:

* Navigate to the **Options** node to enable this feature for all Views in your application. The value you specified in this node is the default for **UseAsyncLoading** in the View-specific nodes.

    ![UseAsyncLoading property in Model Editor](~/images/UseAsyncLoading_Options.png)

* Navigate to the [!include[Template Title](~/templates/node_views_listview111381.md)] node to enable this feature for a specific List View.

    ![UseAsyncLoading property for list view in Model Editor](~/images/UseAsyncLoading_ListView.png)

* Navigate to the [!include[Template Title](~/templates/node_detailview111382.md)] node to enable this feature for a Detail View.

    ![UseAsyncLoading property for detail view in Model Editor](~/images/UseAsyncLoading_DetailView.png)

## Important Notes

### Detail Views

Detail Views always load associated collections in the main thread. These operations lock the UI. If you enable the @DevExpress.ExpressApp.Model.IModelAsync.UseAsyncLoading option, the View loads only its current object asynchronously. In other words, this option only helps you resolve high load times for the current object (for example, when this object has properties with complex logic or you use a remote database).

[!include[DetailView-UseAsyncLoading-notes](~/templates/DetailView-UseAsyncLoading-notes.md)]

### List Views

If you enable the @DevExpress.ExpressApp.Model.IModelAsync.UseAsyncLoading option, do not manipulate a List View's @DevExpress.ExpressApp.IObjectSpace until all data is loaded.