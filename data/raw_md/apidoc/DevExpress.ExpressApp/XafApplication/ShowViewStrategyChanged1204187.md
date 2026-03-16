---
uid: DevExpress.ExpressApp.XafApplication.ShowViewStrategyChanged
name: ShowViewStrategyChanged
type: Event
summary: Occurs when the [XafApplication.ShowViewStrategy](xref:DevExpress.ExpressApp.XafApplication.ShowViewStrategy) object is changed.
syntax:
  content: public event EventHandler<EventArgs> ShowViewStrategyChanged
seealso: []
---
In the **ShowViewStrategyChanged** event handler, you can subscribe to the events of the Show View Strategy, e.g., to the [WinShowViewStrategyBase.WinWindowShowing](xref:DevExpress.ExpressApp.Win.WinShowViewStrategyBase.WinWindowShowing) event. Do not subscribe to these events directly, because the [XafApplication.ShowViewStrategy](xref:DevExpress.ExpressApp.XafApplication.ShowViewStrategy) object can be changed during the application life cycle.