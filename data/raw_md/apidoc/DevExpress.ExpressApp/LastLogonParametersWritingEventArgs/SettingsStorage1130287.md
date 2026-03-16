---
uid: DevExpress.ExpressApp.LastLogonParametersWritingEventArgs.SettingsStorage
name: SettingsStorage
type: Property
summary: Provides access to the settings storage which is used to save logon parameters.
syntax:
  content: public SettingsStorage SettingsStorage { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Utils.SettingsStorage
    description: A **SettingsStorage** object that manages the logon parameters location.
seealso: []
---
Use the object returned by this property to save the logon parameters specified by the [LastLogonParametersWritingEventArgs.LogonObject](xref:DevExpress.ExpressApp.LastLogonParametersWritingEventArgs.LogonObject) property.