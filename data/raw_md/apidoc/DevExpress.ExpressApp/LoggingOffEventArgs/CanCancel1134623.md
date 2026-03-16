---
uid: DevExpress.ExpressApp.LoggingOffEventArgs.CanCancel
name: CanCancel
type: Property
summary: Indicates whether the log off process can be canceled.
syntax:
  content: public bool CanCancel { get; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the log off process can be canceled; otherwise, **false**.'
seealso: []
---
If the log off process has been initiated by a user (via the **Log Off** [LogoffController.LogoffAction](xref:DevExpress.ExpressApp.SystemModule.LogoffController.LogoffAction)), the **CanCancel** property returns **true** and you can cancel the process by setting the [XafApplication.LoggingOff](xref:DevExpress.ExpressApp.XafApplication.LoggingOff) event handler's **Cancel** parameter to **true**.