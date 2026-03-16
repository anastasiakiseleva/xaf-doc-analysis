---
uid: DevExpress.ExpressApp.Model.NodeGenerators.ModelLocalizationGroupGenerator
name: ModelLocalizationGroupGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.Model.IModelLocalizationGroup) node.
syntax:
  content: |-
    [Browsable(false)]
    public class ModelLocalizationGroupGenerator : ModelNodesGeneratorBase
seealso:
- linkId: DevExpress.ExpressApp.Model.NodeGenerators.ModelLocalizationGroupGenerator._members
  altText: ModelLocalizationGroupGenerator Members
- linkId: "112810"
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates child nodes of the **Localization** | **LocalizationGroup** node. Adds [](xref:DevExpress.ExpressApp.Model.IModelLocalizationItem) and nested [](xref:DevExpress.ExpressApp.Model.IModelLocalizationGroup) nodes of the current localization group based on registered **IXafResourceLocalizer** objects.

[!include[<LocalizationGroup><ModelLocalizationGroupGenerator>](~/templates/nodegenerator-example.md)]

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.