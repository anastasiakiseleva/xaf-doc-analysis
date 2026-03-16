---
uid: DevExpress.ExpressApp.Actions.ActionBase.TargetObjectType
name: TargetObjectType
type: Property
summary: Specifies the type of the object(s) that must be represented by the current [View](xref:112611) to provide an [Action](xref:112622) activation.
syntax:
  content: |-
    [DefaultValue(null)]
    public Type TargetObjectType { get; set; }
  parameters: []
  return:
    type: System.Type
    description: The **Type** of the object(s) for which the current Action is intended.
seealso:
- linkId: "113103"
---
If an Action is contained in a View Controller, you can specify the kind of the type of object(s) for which the Action will be activated. For this purpose, use the **TargetObjectType** property. By default, this property is not set. You can set a value in the Controller's constructor or **Designer**. This value will be saved to the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.Model.IModelAction) node.

To make a single Action available in Views of different business object types simultaneously, set the **TargetObjectType** property in code to an interface or their base class type, which is implemented or inherited by all these business types respectively. Alternatively, for the same task, you can specify several View identifiers via the [ActionBase.TargetViewId](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetViewId) property.