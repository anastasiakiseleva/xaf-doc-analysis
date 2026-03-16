---
uid: DevExpress.ExpressApp.Model.NodeGenerators.ModelListViewColumnsNodesGenerator
name: ModelListViewColumnsNodesGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.Model.IModelColumns) node.
syntax:
  content: |-
    [Browsable(false)]
    public class ModelListViewColumnsNodesGenerator : ModelListViewColumnsNodesGeneratorBase<IModelColumn, IModelColumn>
seealso:
- linkId: DevExpress.ExpressApp.Model.NodeGenerators.ModelListViewColumnsNodesGenerator._members
  altText: ModelListViewColumnsNodesGenerator Members
- linkId: "112810"
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates child nodes of the [!include[Node_Views_ListView_Columns](~/templates/node_views_listview_columns111387.md)] node. It adds [](xref:DevExpress.ExpressApp.Model.IModelColumn) nodes that represent columns of the current List View. The rules for generating the default column set are described in the [List View Column Generation](xref:113285) topic.

[!include[<Columns><ModelListViewColumnsNodesGenerator>](~/templates/nodegenerator-example.md)]

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.