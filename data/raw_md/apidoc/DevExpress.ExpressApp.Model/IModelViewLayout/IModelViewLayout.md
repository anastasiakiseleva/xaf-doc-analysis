---
uid: DevExpress.ExpressApp.Model.IModelViewLayout
name: IModelViewLayout
type: Interface
summary: The Layout node defines the layout of View Items in a Composite View.
syntax:
  content: |-
    [ModelNodesGenerator(typeof(ModelDetailViewLayoutNodesGenerator))]
    public interface IModelViewLayout : IModelNode, IModelList<IModelViewLayoutElement>, IList<IModelViewLayoutElement>, ICollection<IModelViewLayoutElement>, IEnumerable<IModelViewLayoutElement>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelViewLayout._members
  altText: IModelViewLayout Members
- linkId: "112579"
- linkId: "112580"
---
The Model Editor used for working with the Application Model allows you to layout View Items in a standard way. When the Layout node is selected, a design surface is displayed on the right, instead of the property list:

![Tutorial_UIC_Lesson21_1](~/images/tutorial_uic_lesson21_1115630.png)

To change the default View Items layout, right-click on the empty space and choose **Customize Layout**. The Customization form will be invoked. Now, you can drag items to the required locations. When finished, close the Customization form.

To learn more about the **Customization** form, the Layout Tree View tab and its context menu, refer to the [Default Runtime Customization](xref:2307) link.

> [!NOTE]
> In addition to the Layout node's nested nodes, there is a [](xref:DevExpress.ExpressApp.Model.IModelLayoutManagerOptions) node, that allows you to specify global settings for Composite View layout.

To learn more about layout in XAF, refer to the [View Items Layout Customization](xref:112817) topic.

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelViewLayout** node represents a list of the [](xref:DevExpress.ExpressApp.Model.IModelViewLayoutElement) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelDetailViewLayoutNodesGenerator) Nodes Generator.