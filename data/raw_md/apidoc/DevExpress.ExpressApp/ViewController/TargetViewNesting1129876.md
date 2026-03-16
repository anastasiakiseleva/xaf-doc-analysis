---
uid: DevExpress.ExpressApp.ViewController.TargetViewNesting
name: TargetViewNesting
type: Property
summary: Specifies whether the [View](xref:112611) for which a View Controller is intended must be root, nested or any.
syntax:
  content: |-
    [DefaultValue(Nesting.Any)]
    public Nesting TargetViewNesting { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Nesting
    description: A [](xref:DevExpress.ExpressApp.Nesting) enumeration value identifying a View kind.
seealso:
- linkId: DevExpress.ExpressApp.ViewController.TargetObjectType
- linkId: DevExpress.ExpressApp.ViewController.TargetViewId
- linkId: DevExpress.ExpressApp.ViewController.TargetViewType
- linkId: "113103"
---
View Controllers are activated for both [Windows and Frames](xref:112608). However, you can specify the View kind to provide a View Controller activation within the Window or Frame via the **TargetViewNesting** property.

> [!NOTE]
> The **TargetViewNesting** property affects only ViewController's activation. [Controller.FrameAssigned](xref:DevExpress.ExpressApp.Controller.FrameAssigned) and other events that are irrelevant to the view nesting always fire.