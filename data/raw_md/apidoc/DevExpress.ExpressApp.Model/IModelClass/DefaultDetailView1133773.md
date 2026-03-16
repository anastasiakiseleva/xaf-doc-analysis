---
uid: DevExpress.ExpressApp.Model.IModelClass.DefaultDetailView
name: DefaultDetailView
type: Property
summary: Specifies what Detail View is displayed for the current object in any scenario, by default.
syntax:
  content: |-
    [DataSourceCriteria("(AsObjectView Is Not Null) And (AsObjectView.ModelClass Is Not Null) And (IsAssignableFromViewModelClass('@This.TypeInfo', AsObjectView))")]
    [DataSourceProperty("Application.Views", new string[]{})]
    IModelDetailView DefaultDetailView { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Model.IModelDetailView
    description: An [](xref:DevExpress.ExpressApp.Model.IModelDetailView) object representing the DetailView node. This node corresponds to the Detail View, displayed for the current object in any scenario, by default.
seealso: []
---
