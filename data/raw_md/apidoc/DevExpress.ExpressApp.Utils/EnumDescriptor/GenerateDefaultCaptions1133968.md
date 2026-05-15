---
uid: DevExpress.ExpressApp.Utils.EnumDescriptor.GenerateDefaultCaptions(DevExpress.ExpressApp.Model.IModelLocalizationGroup,System.Type,DevExpress.ExpressApp.Utils.CompoundNameConvertStyle)
name: GenerateDefaultCaptions(IModelLocalizationGroup, Type, CompoundNameConvertStyle)
type: Method
summary: Generates **LocalizationItem** nodes corresponding to the values of an enumeration.
syntax:
  content: public static void GenerateDefaultCaptions(IModelLocalizationGroup nodeGroup, Type enumType, CompoundNameConvertStyle compoundNameConvertStyle)
  parameters:
  - id: nodeGroup
    type: DevExpress.ExpressApp.Model.IModelLocalizationGroup
    description: An [](xref:DevExpress.ExpressApp.Model.IModelLocalizationGroup) object representing the **LocalizationGroup** node where **LocalizationItem** child nodes will be created.
  - id: enumType
    type: System.Type
    description: A [](xref:System.Type) object representing the enumeration for which **LocalizationItem** nodes will be generated.
  - id: compoundNameConvertStyle
    type: DevExpress.ExpressApp.Utils.CompoundNameConvertStyle
    description: A [](xref:DevExpress.ExpressApp.Utils.CompoundNameConvertStyle) enumeration value specifying how enumeration values are converted into the **LocalizationItem** nodes' [IModelLocalizationItem.Value](xref:DevExpress.ExpressApp.Model.IModelLocalizationItem.Value) property values.
seealso: []
---
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
            typeof(MyEnum).FullName), typeof(MyEnum), 
            CompoundNameConvertStyle.SplitAndCapitalization);
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp.Model
Imports DevExpress.ExpressApp.Model.Core
Imports DevExpress.ExpressApp.Model.NodeGenerators
'...
Public Enum MyEnum
    FirstEnumValue
    SecondEnumValue
End Enum

Public Class MyEnumUpdater
    Inherits ModelNodesGeneratorUpdater(Of ModelLocalizationNodesGenerator)
    Public Overrides Sub UpdateNode(ByVal node As ModelNode)
        EnumDescriptor.GenerateDefaultCaptions(node("Enums").AddNode(Of IModelLocalizationGroup) _
        (GetType(MyEnum).FullName), GetType(MyEnum), _
        CompoundNameConvertStyle.SplitAndCapitalization)
    End Sub
End Class
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

# [VB.NET](#tab/tabid-vb)

```vb
Public NotInheritable Partial Class MainDemoModule
    Inherits ModuleBase
    '...
    Public Overrides Sub AddGeneratorUpdaters( _
    ByVal updaters As DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)
        MyBase.AddGeneratorUpdaters(updaters)
        updaters.Add(New MyEnumUpdater())
    End Sub
End Class
```

***

This will generate a new group under the **Localization** | **Enums** node.

![EnumDescriptor_GenerateDefaultCaptions](~/images/enumdescriptor_generatedefaultcaptions116684.png)