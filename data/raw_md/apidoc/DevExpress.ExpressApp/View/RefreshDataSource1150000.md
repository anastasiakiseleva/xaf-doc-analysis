---
uid: DevExpress.ExpressApp.View.RefreshDataSource
name: RefreshDataSource()
type: Method
summary: Refreshes the data source of the current [](xref:DevExpress.ExpressApp.View).
syntax:
  content: public virtual void RefreshDataSource()
seealso: []
---
To refresh the data source together with the [View](xref:112611)'s control values, use the [View.Refresh](xref:DevExpress.ExpressApp.View.Refresh*) method with the _refreshDataSource_ parameter.

This method is overloaded in [](xref:DevExpress.ExpressApp.View) descendants in the following way:

| Method Overload | Description |
|---|---|
| [ListView.RefreshDataSource](xref:DevExpress.ExpressApp.ListView.RefreshDataSource) | Calls the [CollectionSourceBase.Reload](xref:DevExpress.ExpressApp.CollectionSourceBase.Reload) method. |
| [DetailView.RefreshDataSource](xref:DevExpress.ExpressApp.DetailView.RefreshDataSource) | Calls the [IObjectSpace.ReloadObject](xref:DevExpress.ExpressApp.IObjectSpace.ReloadObject(System.Object)) method and passes the [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject) object to it. |