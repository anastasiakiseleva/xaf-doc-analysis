---
uid: DevExpress.ExpressApp.Model.IModelColumns
name: IModelColumns
type: Interface
summary: The Columns node provides access to a List View's columns.
syntax:
  content: |-
    [ModelNodesGenerator(typeof(ModelListViewColumnsNodesGenerator))]
    public interface IModelColumns : IModelNode, IModelList<IModelColumn>, IList<IModelColumn>, ICollection<IModelColumn>, IEnumerable<IModelColumn>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelColumns._members
  altText: IModelColumns Members
- linkId: "112579"
- linkId: "112580"
- linkId: "113285"
---
When the Layout node is selected in the [Model Editor](xref:112582), a design surface is displayed on the right, instead of the property list:

![Tutorial_UIC_Lesson16_1](~/images/tutorial_uic_lesson16_1115506.png)

To learn more, refer to the [List View Columns Customization](xref:113679) topic.

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelColumns** node represents a list of the [](xref:DevExpress.ExpressApp.Model.IModelColumn) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelListViewColumnsNodesGenerator) Nodes Generator.