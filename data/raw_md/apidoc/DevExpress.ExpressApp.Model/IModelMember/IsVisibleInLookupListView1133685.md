---
uid: DevExpress.ExpressApp.Model.IModelMember.IsVisibleInLookupListView
name: IsVisibleInLookupListView
type: Property
summary: Specifies whether the current property is displayed in Lookup List Views, together with the default lookup property.
syntax:
  content: |-
    [Browsable(false)]
    [DefaultValue(false)]
    bool? IsVisibleInLookupListView { get; }
  parameters: []
  return:
    type: System.Nullable{System.Boolean}
    description: '**true**, if the current property is displayed in Lookup List Views, together with the default lookup property; otherwise, **false**.'
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelClass.DefaultProperty
---
This property can be set in code, using the [](xref:DevExpress.Persistent.Base.VisibleInLookupListViewAttribute).