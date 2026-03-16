---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceRulesModelNodesGenerator
name: AppearanceRulesModelNodesGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.ConditionalAppearance.IModelAppearanceRules) node.
syntax:
  content: 'public class AppearanceRulesModelNodesGenerator : ModelNodesGeneratorBase'
seealso:
- linkId: DevExpress.ExpressApp.ConditionalAppearance.AppearanceRulesModelNodesGenerator._members
  altText: AppearanceRulesModelNodesGenerator Members
- linkId: "112810"
- linkId: "113286"
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates child nodes of a **BOModel** | **_\<Class\>_** | **AppearanceRules** node. It collects [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute) attributes applied in a business class code, and adds corresponding [](xref:DevExpress.ExpressApp.ConditionalAppearance.IModelAppearanceRule) nodes.

[!include[<AppearanceRules><AppearanceRulesModelNodesGenerator>](~/templates/nodegenerator-example.md)]

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.