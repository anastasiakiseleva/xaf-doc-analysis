---
uid: DevExpress.ExpressApp.Model.NodeGenerators.ModelBOModelMemberNodesGenerator
name: ModelBOModelMemberNodesGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.Model.IModelBOModelClassMembers) node.
syntax:
  content: 'public class ModelBOModelMemberNodesGenerator : ModelNodesGeneratorBase'
seealso:
- linkId: DevExpress.ExpressApp.Model.NodeGenerators.ModelBOModelMemberNodesGenerator._members
  altText: ModelBOModelMemberNodesGenerator Members
- linkId: "112810"
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates child nodes of **BOModel** | **OwnMembers** nodes. It gets a public members list from the business class' metadata information. It initializes the [](xref:DevExpress.ExpressApp.Model.IModelMember) nodes' properties with values specified in code via [Data Annotations in Data Model](xref:112701) applied to business class members, e.g [](xref:DevExpress.Xpo.CustomAttribute), [](xref:DevExpress.Persistent.Base.IndexAttribute), [](xref:DevExpress.Persistent.Base.LookupEditorModeAttribute), [](xref:DevExpress.Persistent.Base.ImagesForBoolValuesAttribute), [](xref:DevExpress.Persistent.Base.CaptionsForBoolValuesAttribute), [](xref:DevExpress.Persistent.Base.ImageEditorAttribute), [](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute), etc.

[!include[<OwnMembers><ModelBOModelMemberNodesGenerator>](~/templates/nodegenerator-example.md)]

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.