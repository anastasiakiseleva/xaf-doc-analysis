---
uid: DevExpress.ExpressApp.SystemModule.IModelListViewFilters.CurrentFilter
name: CurrentFilter
type: Property
summary: Specifies a filter that must be applied to the current List View.
syntax:
  content: |-
    [DataSourceProperty("this", new string[]{})]
    IModelListViewFilterItem CurrentFilter { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.SystemModule.IModelListViewFilterItem
    description: An [](xref:DevExpress.ExpressApp.SystemModule.IModelListViewFilterItem) object specifying a filter that must be applied to the current List View.
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.FilterController
---
If this property is not set, the List View is not filtered.