---
uid: DevExpress.ExpressApp.IObjectSpace.GetEvaluatorContextDescriptor(System.Type)
name: GetEvaluatorContextDescriptor(Type)
type: Method
summary: Creates an instance of the **EvaluatorContextDescriptor** that is used to supply metadata on the specified type to the **ExpressionEvaluator** objects.
syntax:
  content: EvaluatorContextDescriptor GetEvaluatorContextDescriptor(Type type)
  parameters:
  - id: type
    type: System.Type
    description: A type for which an instance of the **EvaluatorContextDescriptor** class must be created.
  return:
    type: DevExpress.Data.Filtering.Helpers.EvaluatorContextDescriptor
    description: An **EvaluatorContextDescriptor** object initialized for the specified type.
seealso: []
---
When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you don't have to implement this method. The **BaseObjectSpace.GetEvaluatorContextDescriptor** method creates an instance of the **DevExpress.Data.Filtering.Helpers.EvaluatorContextDescriptorDefault** class. However, if you need to create a custom descriptor, override the **BaseObjectSpace.GetEvaluatorContextDescriptor** method.