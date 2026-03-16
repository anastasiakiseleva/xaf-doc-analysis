---
uid: DevExpress.ExpressApp.CloneObject.CustomGetCloneActionTargetTypesEventArgs.GetDefaultTargetTypes
name: GetDefaultTargetTypes()
type: Method
summary: Returns the default target types of the [CloneObjectViewController.CloneObjectAction](xref:DevExpress.ExpressApp.CloneObject.CloneObjectViewController.CloneObjectAction).
syntax:
  content: public Dictionary<IModelNode, Type> GetDefaultTargetTypes()
  return:
    type: System.Collections.Generic.Dictionary{DevExpress.ExpressApp.Model.IModelNode,System.Type}
    description: A **Dictionary\<**[](xref:DevExpress.ExpressApp.Model.IModelNode)**, Type>** object that describes the default target types of the **CloneObject** [Action](xref:112622), and their corresponding BOModel | Class [Application Model](xref:112580) nodes.
seealso: []
---
The `GetDefaultTargetTypes` method returns a new list each time it is called. To avoid performance issues, you should cache the list returned by this method.