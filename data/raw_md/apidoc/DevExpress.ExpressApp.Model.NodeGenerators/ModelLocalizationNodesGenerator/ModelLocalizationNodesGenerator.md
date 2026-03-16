---
uid: DevExpress.ExpressApp.Model.NodeGenerators.ModelLocalizationNodesGenerator
name: ModelLocalizationNodesGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.Model.IModelLocalization) node.
syntax:
  content: |-
    [Browsable(false)]
    public class ModelLocalizationNodesGenerator : ModelNodesGeneratorBase
seealso:
- linkId: DevExpress.ExpressApp.Model.NodeGenerators.ModelLocalizationNodesGenerator._members
  altText: ModelLocalizationNodesGenerator Members
- linkId: "112810"
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates first-level child nodes ([](xref:DevExpress.ExpressApp.Model.IModelLocalizationItem) nodes) of the **Localization** node, based on registered **IXafResourceLocalizer** objects.

[!include[<Localization><ModelLocalizationNodesGenerator>](~/templates/nodegenerator-example.md)]

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method. The complete example of implementing a Generator Updater for this Nodes Generator is provided in the [EnumDescriptor.GenerateDefaultCaptions](xref:DevExpress.ExpressApp.Utils.EnumDescriptor.GenerateDefaultCaptions*) topic.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.