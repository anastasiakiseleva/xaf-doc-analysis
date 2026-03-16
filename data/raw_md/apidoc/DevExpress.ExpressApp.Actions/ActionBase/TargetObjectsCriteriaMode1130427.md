---
uid: DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteriaMode
name: TargetObjectsCriteriaMode
type: Property
summary: Specifies whether all the currently selected objects must satisfy the [ActionBase.TargetObjectsCriteria](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteria) criteria to make an Action enabled.
syntax:
  content: |-
    [DefaultValue(TargetObjectsCriteriaMode.TrueAtLeastForOne)]
    public TargetObjectsCriteriaMode TargetObjectsCriteriaMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.TargetObjectsCriteriaMode
    description: A **TargetObjectsCriteriaMode** enumeration value that indicates whether all selected object or at least one of them must satisfy the [ActionBase.TargetObjectsCriteria](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteria) criteria.
seealso:
- linkId: DevExpress.ExpressApp.DetailView.SelectedObjects
- linkId: DevExpress.ExpressApp.ListView.SelectedObjects
- linkId: "113103"
---
When specifying the [ActionBase.TargetObjectsCriteria](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteria) property, specify the **TargetObjectsCriteriaMode** property as well. The following values are available:

* **TrueAtLeastForOne**
    
    At least one of the selected objects must satisfy the criteria specified by the [ActionBase.TargetObjectsCriteria](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteria) property to make the Action enabled.
* **TrueForAll**
    
    All the selected objects must satisfy the criteria specified by the [ActionBase.TargetObjectsCriteria](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteria) property to make the Action enabled.