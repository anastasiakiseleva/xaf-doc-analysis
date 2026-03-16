---
uid: DevExpress.ExpressApp.Utils.EnumDescriptor.GenerateDefaultCaptions(DevExpress.ExpressApp.Model.IModelLocalizationGroup,System.Type)
name: GenerateDefaultCaptions(IModelLocalizationGroup, Type)
type: Method
summary: Generates **LocalizationItem** nodes corresponding to the values of an enumeration.
syntax:
  content: public static void GenerateDefaultCaptions(IModelLocalizationGroup nodeGroup, Type enumType)
  parameters:
  - id: nodeGroup
    type: DevExpress.ExpressApp.Model.IModelLocalizationGroup
    description: An [](xref:DevExpress.ExpressApp.Model.IModelLocalizationGroup) object representing the **LocalizationGroup** node where **LocalizationItem** child nodes will be created.
  - id: enumType
    type: System.Type
    description: A [](xref:System.Type) object representing the enumeration for which **LocalizationItem** nodes will be generated.
seealso: []
---
Calling this **GenerateDefaultCaptions** method overload is equivalent to calling the **GenerateDefaultCaptions** method overload that takes the _compoundNameConvertStyle_ parameter, with the [CompoundNameConvertStyle.SplitAndCapitalization](xref:DevExpress.ExpressApp.Utils.CompoundNameConvertStyle.SplitAndCapitalization) value.

Since localization nodes for enumerations used as types of persistent properties are automatically generated, generally, you do not need to use the **GenerateDefaultCaptions** method. Nevertheless, you can use this method to create localization nodes for an arbitrary enumeration by [implementing a Generator Updater](xref:112810). The following code snippet illustrates this.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.Model.Core;
using DevExpress.ExpressApp.Model.NodeGenerators;
//...
public enum MyEnum {
    FirstEnumValue,
    SecondEnumValue
}
public class MyEnumUpdater : ModelNodesGeneratorUpdater<ModelLocalizationNodesGenerator> {
    public override void UpdateNode(ModelNode node) {
        EnumDescriptor.GenerateDefaultCaptions(node["Enums"].AddNode<IModelLocalizationGroup>(
            typeof(MyEnum).FullName), typeof(MyEnum));
    }
}
```
***

To register the Generator Updater, the [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method should be overridden.

# [C#](#tab/tabid-csharp)

```csharp
public sealed partial class MyModule : ModuleBase {
    //...
    public override void AddGeneratorUpdaters(
        DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters updaters) {
        base.AddGeneratorUpdaters(updaters);
        updaters.Add(new MyEnumUpdater());
    }
}
```
***

This will generate a new group under the **Localization** | **Enums** node.

![EnumDescriptor_GenerateDefaultCaptions](~/images/enumdescriptor_generatedefaultcaptions116684.png)