---
uid: DevExpress.ExpressApp.Editors.ViewItem.RefreshDataSource
name: RefreshDataSource()
type: Method
summary: Refreshes the data source of the current [](xref:DevExpress.ExpressApp.Editors.ViewItem).
syntax:
  content: public virtual void RefreshDataSource()
seealso: []
---
To refresh the data source together with the [View](xref:112611)'s control value, use the [View.Refresh](xref:DevExpress.ExpressApp.View.Refresh*) method with the _refreshDataSource_ parameter.

This method is overloaded in [](xref:DevExpress.ExpressApp.Editors.ViewItem) descendants in the following way:

| Method Overload | Description |
|---|---|
| **ListPropertyEditor.RefreshDataSource** | Calls the [ListView.RefreshDataSource](xref:DevExpress.ExpressApp.ListView.RefreshDataSource) method. |
| **DetailPropertyEditor.RefreshDataSource** | Calls the [DetailView.RefreshDataSource](xref:DevExpress.ExpressApp.DetailView.RefreshDataSource) method. |