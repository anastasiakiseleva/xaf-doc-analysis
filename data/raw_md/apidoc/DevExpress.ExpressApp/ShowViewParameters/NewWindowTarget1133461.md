---
uid: DevExpress.ExpressApp.ShowViewParameters.NewWindowTarget
name: NewWindowTarget
type: Property
summary: Specifies whether to invoke the target [View](xref:112611) in a new tab/MDI child Window of the main [Window](xref:112608) or in a separate [Window](xref:112608).
syntax:
  content: |-
    [DefaultValue(NewWindowTarget.Default)]
    public NewWindowTarget NewWindowTarget { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.NewWindowTarget
    description: The Window in which the View should be invoked.
seealso: []
---
When the application displays a multiple document interface (the `UIType` property is set to `TabbedMDI` or `StandardMDI`) and the @DevExpress.ExpressApp.ShowViewParameters.TargetWindow property is set to `NewWindow` or `Default`, use the `NewWindowTarget` property to specify where to display the target View.