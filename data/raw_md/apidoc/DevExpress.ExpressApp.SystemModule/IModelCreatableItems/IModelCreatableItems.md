---
uid: DevExpress.ExpressApp.SystemModule.IModelCreatableItems
name: IModelCreatableItems
type: Interface
summary: The **CreatableItems** node provides information to the **New** Action in WinForms.
syntax:
  content: |-
    [ImageName("ModelEditor_CreatableItems_Object")]
    [ModelNodesGenerator(typeof(ModelCreatableItemsGenerator))]
    public interface IModelCreatableItems : IModelNode, IModelList<IModelCreatableItem>, IList<IModelCreatableItem>, ICollection<IModelCreatableItem>, IEnumerable<IModelCreatableItem>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.IModelCreatableItems._members
  altText: IModelCreatableItems Members
- linkId: "112579"
- linkId: "112580"
---
This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases. The `IModelCreatableItems` is used by the [](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController), to extend the [](xref:DevExpress.ExpressApp.Model.IModelApplication). To learn more, refer to the  [Application Model Structure](xref:112580) topic.

The `IModelCreatableItems` interface is a list of the [](xref:DevExpress.ExpressApp.SystemModule.IModelCreatableItem) nodes.

The **CreatableItems** node contains additional items for the **New** Action in WinForms. In this platform, the **New** Action's items are divided in the following groups.


![WinNewObjectViewController_New](~/images/winnewobjectviewcontroller_new115926.png)

The group that is displayed above the separator represents the current List View's object type and its descendants. The group below the separator contains the items that are listed in the CreatableItems node.

Use the **CreatableItems** node to add items to the New Action. The items are represented by this node's child nodes. To add a new child node, select the **Add Item** menu item in the CreatableItems node' context menu.

You can add child nodes to the **CreatableItems** node in code. Use the [](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) or [](xref:DevExpress.Persistent.Base.CreatableItemAttribute) attribute for this purpose.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.SystemModule.ModelCreatableItemsGenerator) Nodes Generator.