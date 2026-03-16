---
uid: DevExpress.ExpressApp.LastLogonParametersWritingEventArgs.DetailView
name: DetailView
type: Property
summary: Provides access to the [Detail View](xref:112611) displayed on the current logon [Window](xref:112608).
syntax:
  content: public DetailView DetailView { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.DetailView
    description: A [](xref:DevExpress.ExpressApp.DetailView) object that represents the Detail View of the current logon Window.
seealso: []
---
You can use a logon Window's Detail View as a source of the current logon parameters instead of the [LastLogonParametersWritingEventArgs.LogonObject](xref:DevExpress.ExpressApp.LastLogonParametersWritingEventArgs.LogonObject) property values. Save values of the [View Items](xref:112612) via the object specified via the [LastLogonParametersWritingEventArgs.SettingsStorage](xref:DevExpress.ExpressApp.LastLogonParametersWritingEventArgs.SettingsStorage) property.