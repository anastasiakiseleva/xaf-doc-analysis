---
uid: DevExpress.ExpressApp.Model.IModelClass.DefaultLookupListView
name: DefaultLookupListView
type: Property
summary: Specifies what Lookup List View is displayed for the current object in any scenario, by default.
syntax:
  content: |-
    [DataSourceCriteria("(AsObjectView Is Not Null) And (AsObjectView.ModelClass Is Not Null) And (IsAssignableFromViewModelClass('@This.TypeInfo', AsObjectView))")]
    [DataSourceProperty("Application.Views", new string[]{})]
    IModelListView DefaultLookupListView { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Model.IModelListView
    description: A string holding the [IModelView.Id](xref:DevExpress.ExpressApp.Model.IModelView.Id) of the Lookup List View that is displayed for the current object in any scenario, by default.
seealso:
- linkId: DevExpress.ExpressApp.View.Id
---
