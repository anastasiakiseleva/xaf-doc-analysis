---
uid: DevExpress.Persistent.Base.ActionAttribute.SelectionDependencyType
name: SelectionDependencyType
type: Property
summary: Specifies a context for enabling the generated Action.
syntax:
  content: public MethodActionSelectionDependencyType SelectionDependencyType { get; set; }
  parameters: []
  return:
    type: DevExpress.Persistent.Base.MethodActionSelectionDependencyType
    description: A [](xref:DevExpress.Persistent.Base.MethodActionSelectionDependencyType) enumeration value identifying a context type.
seealso: []
---
Use this property to specify the availability context for the Action which will be generated from the Action attribute's target method. By default, this property is set to [MethodActionSelectionDependencyType.RequireMultipleObjects](xref:DevExpress.Persistent.Base.MethodActionSelectionDependencyType.RequireMultipleObjects).