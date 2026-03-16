---
uid: DevExpress.ExpressApp.Model.ModelNodesGeneratorAttribute
name: ModelNodesGeneratorAttribute
type: Class
summary: Applied to [Application Model](xref:112580) node interfaces. Specifies a [Nodes Generator](xref:112810) for the current node.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Interface)]
    public sealed class ModelNodesGeneratorAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.Model.ModelNodesGeneratorAttribute._members
  altText: ModelNodesGeneratorAttribute Members
- linkId: "112810"
---
To define how the custom Application Model node is generated, implement a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant and  override the **GenerateNodesCore** method. To apply the implemented Generator to the required node, decorate the model node interface with the **ModelNodesGenerator** attribute, and pass the Nodes Generator type as the parameter.

# [C#](#tab/tabid-csharp)

```csharp
[ModelNodesGenerator(typeof(MyChildNodesGenerator))]
public interface IModelMyNodeWithChildNodes : IModelNode, IModelList<IModelMyChildNode> {
}
```
***