---
uid: DevExpress.ExpressApp.XafApplication.PropertyChanged
name: PropertyChanged
type: Event
summary: Occurs when the [XafApplication.ApplicationName](xref:DevExpress.ExpressApp.XafApplication.ApplicationName), [XafApplication.Security](xref:DevExpress.ExpressApp.XafApplication.Security) or [XafApplication.Connection](xref:DevExpress.ExpressApp.XafApplication.Connection) property is changed.
syntax:
  content: |-
    [Browsable(false)]
    public event PropertyChangedEventHandler PropertyChanged
seealso: []
---
To determine what property has changed, use the handler's **PropertyChangedEventArgs.PropertyName** parameter.