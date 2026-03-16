---
uid: DevExpress.ExpressApp.ShowViewStrategyBase.SupportViewNavigationHistory
name: SupportViewNavigationHistory
type: Property
summary: Indicates whether the Show View Strategy keeps track of invoked [Views](xref:112611).
syntax:
  content: public virtual bool SupportViewNavigationHistory { get; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the Show View Strategy keeps track of invoked Views; otherwise, **false**. The default value is **true**.'
seealso: []
---
This property is used by the [ViewNavigationController](xref:113141), to decide whether the Back and Forward Actions should be enabled. These Actions allow end-users to navigate to recently invoked Views. If the **SupportViewNavigationHistory** property of the currently active Show View Strategy returns false, the Back and Forward Actions are disabled.