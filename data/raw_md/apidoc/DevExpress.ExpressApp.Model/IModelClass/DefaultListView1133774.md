---
uid: DevExpress.ExpressApp.Model.IModelClass.DefaultListView
name: DefaultListView
type: Property
summary: Specifies what List View is displayed for the current object in any scenario, by default.
syntax:
  content: |-
    [DataSourceCriteria("(AsObjectView Is Not Null) And (AsObjectView.ModelClass Is Not Null) And (IsAssignableFromViewModelClass('@This.TypeInfo', AsObjectView))")]
    [DataSourceProperty("Application.Views", new string[]{})]
    IModelListView DefaultListView { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Model.IModelListView
    description: An [](xref:DevExpress.ExpressApp.Model.IModelListView) object representing the ListView node. This node corresponds to the  List View which is displayed for the current object in any scenario, by default.
seealso: []
---
