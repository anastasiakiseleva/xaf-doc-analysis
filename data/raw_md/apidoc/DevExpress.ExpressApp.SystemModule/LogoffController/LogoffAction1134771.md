---
uid: DevExpress.ExpressApp.SystemModule.LogoffController.LogoffAction
name: LogoffAction
type: Property
summary: Provides access to the **Logoff** [Action](xref:112622).
syntax:
  content: public SimpleAction LogoffAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) object representing the **Log Off** Action.
seealso: []
---
The **Logoff** Action allows end-users to log off from the application.

![LogOffAction_Web](~/images/logoffaction_web116266.png)

![LogOffAction_Win](~/images/logoffaction_win116762.png)

The **Logoff** Action is activated when the Security System's **IsLogoffEnabled** property returns **true**. This occurs when the Authentication strategy, which is used by the current security system, enables logging off. By default, the Standard Authentication strategy permits logging off, while the Active Directory Authentication strategy prohibits this. The **Log Off** Action's **Execute** event is handled by the **LogoffControllerBase**'s **Logoff** protected method.

To ascertain why the **Logoff** Action is currently deactivated or disabled, use the [DiagnosticInfo](xref:112818) Action. If you need to change the Action's "active" or "enabled" state in code, use its [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) or [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property, respectively. Information on the **Logoff** Action is also available in the [Application Model](xref:112580)'s **ActionDesign** node. You can access it, using the [Model Editor.Application Model](xref:112582).

The [](xref:DevExpress.ExpressApp.XafApplication) class exposes two events related to the **Log Off** Action. The [XafApplication.LoggingOff](xref:DevExpress.ExpressApp.XafApplication.LoggingOff) event is raised after a user has clicked the **Log Off** button, and allows you to cancel the log off process. The [XafApplication.LoggedOff](xref:DevExpress.ExpressApp.XafApplication.LoggedOff) event is raised after a user has logged off, and allows you to perform custom actions.