---
uid: DevExpress.ExpressApp.Actions.ActionBase.Available
name: Available
type: Property
summary: Identifies whether the Action is enabled and active.
syntax:
  content: |-
    [Browsable(false)]
    public bool Available { get; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if the Action is enabled and active; otherwise, `false`'
seealso: []
---
Action availability is determined by the @DevExpress.ExpressApp.Actions.ActionBase.Active and @DevExpress.ExpressApp.Actions.ActionBase.Enabled properties.