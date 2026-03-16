---
uid: DevExpress.ExpressApp.Model.ModelNodesGeneratorBase
name: ModelNodesGeneratorBase
type: Class
summary: The base class for [Nodes Generators](xref:112810).
syntax:
  content: public abstract class ModelNodesGeneratorBase
seealso:
- linkId: DevExpress.ExpressApp.Model.ModelNodesGeneratorBase._members
  altText: ModelNodesGeneratorBase Members
---
To define how the custom Application Model node is generated, inherit this class and override the **GenerateNodesCore** method. To access the node for which the generator is invoked, use the method's _node_ parameter. To apply the implemented Generator to the required node, decorate the model node interface with the [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorAttribute) attribute, and pass the Nodes Generator type as the parameter. The code example is provided in the [Extend and Customize the Application Model in Code](xref:112810).

If you cannot modify the Nodes Generator code (for instance, if it is one of the [built-in Nodes Generators](xref:113316)), you still can customize the generated node content in code. Implement a Generator Updater by inheriting the [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorUpdater`1) class. The complete example of implementing Generator Updaters for this Nodes Generator is provided in the [How to: Create Additional ListView Nodes in Code using a Generator Updater](xref:113315) topic.

> [!IMPORTANT]
> [!include[UpdateParentNodesNote](~/templates/updateparentnodesnote111861.md)]