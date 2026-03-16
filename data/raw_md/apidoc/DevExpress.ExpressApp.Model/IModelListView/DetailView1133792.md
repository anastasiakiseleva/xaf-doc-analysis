---
uid: DevExpress.ExpressApp.Model.IModelListView.DetailView
name: DetailView
type: Property
summary: Specifies the List View's Detail View.
syntax:
  content: |-
    [DataSourceCriteria("(AsObjectView Is Not Null) And (AsObjectView.ModelClass Is Not Null) And ('@This.ModelClass' Is Not Null) And (IsAssignableFromViewModelClass('@This.ModelClass.TypeInfo', AsObjectView))")]
    [DataSourceProperty("Application.Views", new string[]{})]
    IModelDetailView DetailView { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Model.IModelDetailView
    description: An [](xref:DevExpress.ExpressApp.Model.IModelDetailView) representing the DetailView node. This node corresponds to the current List View's Detail View.
seealso: []
---
The Detail View specified by this property is:

* Invoked after clicking (in ASP.NET Core Blazor) or double-clicking (in WinForms) on a List View row.
    > [!NOTE]
    > This is true only if the type of the displayed object equals the current List View's object type. If a descendant is shown, XAF uses its Detail View and ignores the `DetailView` property.
* Displayed together with the current List View when the [IModelListView.MasterDetailMode](xref:DevExpress.ExpressApp.Model.IModelListView.MasterDetailMode) is set to `ListViewAndDetailView` and [IModelListView.MasterDetailView](xref:DevExpress.ExpressApp.Model.IModelListView.MasterDetailView) is unspecified.

If the `DetailView` property is not set, XAF uses the default Detail View specified by the [IModelClass.DefaultDetailView](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultDetailView) property.