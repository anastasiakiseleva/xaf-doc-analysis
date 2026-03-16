---
uid: DevExpress.ExpressApp.SystemModule.IModelListViewFilters
name: IModelListViewFilters
type: Interface
summary: The Filters node provides access to the filters that can be applied to a List View.
syntax:
  content: |-
    [ModelNodesGenerator(typeof(ModelListViewFiltersGenerator))]
    public interface IModelListViewFilters : IModelNode, IModelList<IModelListViewFilterItem>, IList<IModelListViewFilterItem>, ICollection<IModelListViewFilterItem>, IEnumerable<IModelListViewFilterItem>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.IModelListViewFilters._members
  altText: IModelListViewFilters Members
- linkId: "112579"
- linkId: "112998"
---
To define a filter, add the Filter child node via the context menu's **Add Filter** menu item.

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelListViewFilters** node represents a list of the [](xref:DevExpress.ExpressApp.SystemModule.IModelListViewFilterItem) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.SystemModule.ModelListViewFiltersGenerator) Nodes Generator.