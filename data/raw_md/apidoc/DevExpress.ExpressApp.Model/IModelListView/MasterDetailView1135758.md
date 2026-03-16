---
uid: DevExpress.ExpressApp.Model.IModelListView.MasterDetailView
name: MasterDetailView
type: Property
summary: Specifies the [Detail View](xref:112611) that is displayed in [MasterDetailMode.ListViewAndDetailView](xref:DevExpress.ExpressApp.MasterDetailMode.ListViewAndDetailView) mode.
syntax:
  content: |-
    [DataSourceCriteria("(AsObjectView Is Not Null) And (AsObjectView.ModelClass Is Not Null) And ('@This.ModelClass' Is Not Null) And (IsAssignableFromViewModelClass('@This.ModelClass.TypeInfo', AsObjectView))")]
    [DataSourceProperty("Application.Views", new string[]{})]
    IModelDetailView MasterDetailView { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Model.IModelDetailView
    description: An [](xref:DevExpress.ExpressApp.Model.IModelDetailView) object, which is the DetailView node defining a Detail View to be displayed in the ListViewAndDetailView mode.
seealso: []
---
If this property is unspecified, then the [IModelListView.DetailView](xref:DevExpress.ExpressApp.Model.IModelListView.DetailView) value is used to determine the Detail View to be displayed. If both the **MasterDetailView** and **DetailView** properties are unspecified, then the Detail View is determined based on the type of the object created or edited via the List View (the [IModelClass.DefaultDetailView](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultDetailView) value specified for a particular object type is used).

You can create a custom Detail View for a particular selected object or a particular List View by handling the [ListView.CreateCustomCurrentObjectDetailView](xref:DevExpress.ExpressApp.ListView.CreateCustomCurrentObjectDetailView) event.