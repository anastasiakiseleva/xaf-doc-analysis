---
uid: DevExpress.ExpressApp.ViewController.TypeOfView
name: TypeOfView
type: Property
summary: Specifies the type of the [View](xref:112611), for which a View Controller is intended.
syntax:
  content: |-
    [Browsable(false)]
    public Type TypeOfView { get; set; }
  parameters: []
  return:
    type: System.Type
    description: A [](xref:System.Type) object identifying a View type.
seealso:
- linkId: DevExpress.ExpressApp.ViewController.TargetObjectType
- linkId: DevExpress.ExpressApp.ViewController.TargetViewId
- linkId: DevExpress.ExpressApp.ViewController.TargetViewNesting
---
View Controllers are activated for both [Windows and Frames](xref:112608). However, you can use the **TypeOfView** property to specify the View type to provide a View Controller activation within the Window or Frame.