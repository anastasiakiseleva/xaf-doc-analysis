---
uid: DevExpress.ExpressApp.Model.NodeGenerators.ModelBOModelClassNodesGenerator
name: ModelBOModelClassNodesGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.Model.IModelBOModel) node.
syntax:
  content: 'public class ModelBOModelClassNodesGenerator : ModelNodesGeneratorBase'
seealso:
- linkId: DevExpress.ExpressApp.Model.NodeGenerators.ModelBOModelClassNodesGenerator._members
  altText: ModelBOModelClassNodesGenerator Members
- linkId: "112810"
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates child nodes of the **BOModel** node. It adds an [](xref:DevExpress.ExpressApp.Model.IModelClass) node for each business class and initializes these **Class** node's properties: [IModelClass.Caption](xref:DevExpress.ExpressApp.Model.IModelClass.Caption), [IModelClass.DefaultListView](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultListView), [IModelClass.DefaultLookupListView](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultLookupListView), [IModelClass.DefaultDetailView](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultDetailView), and properties whose values are specified in code using the [](xref:DevExpress.Xpo.CustomAttribute).

[!include[<BOModel><ModelBOModelClassNodesGenerator>](~/templates/nodegenerator-example.md)]

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.