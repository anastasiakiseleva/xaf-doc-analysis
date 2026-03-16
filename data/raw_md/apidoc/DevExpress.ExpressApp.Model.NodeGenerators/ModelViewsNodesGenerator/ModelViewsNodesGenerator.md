---
uid: DevExpress.ExpressApp.Model.NodeGenerators.ModelViewsNodesGenerator
name: ModelViewsNodesGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.Model.IModelViews) node.
syntax:
  content: |-
    [Browsable(false)]
    public class ModelViewsNodesGenerator : ModelNodesGeneratorBase
seealso:
- linkId: DevExpress.ExpressApp.Model.NodeGenerators.ModelViewsNodesGenerator._members
  altText: ModelViewsNodesGenerator Members
- linkId: "112810"
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates child nodes of the **Views** node. Adds an [](xref:DevExpress.ExpressApp.Model.IModelDetailView) and two [](xref:DevExpress.ExpressApp.Model.IModelListView) nodes for each class defined in the [](xref:DevExpress.ExpressApp.Model.IModelBOModel) node. One of the generated **ListView** nodes defines a general-purpose List View, and another - a Lookup List View.

[!include[<Views><ModelViewsNodesGenerator>](~/templates/nodegenerator-example.md)]

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method. The complete example of implementing Generator Updaters for this Nodes Generator is provided in the [How to: Create Additional ListView Nodes in Code using a Generator Updater](xref:113315) topic.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.