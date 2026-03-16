---
uid: DevExpress.ExpressApp.LastLogonParametersReadingEventArgs.SettingsStorage
name: SettingsStorage
type: Property
summary: Provides access to the settings storage which is used to load logon parameters.
syntax:
  content: public SettingsStorage SettingsStorage { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Utils.SettingsStorage
    description: A **SettingsStorage** object that manages the logon parameters location.
seealso: []
---
Use the object returned by this property to load last logon parameters to the object specified by the [LastLogonParametersReadingEventArgs.LogonObject](xref:DevExpress.ExpressApp.LastLogonParametersReadingEventArgs.LogonObject) property.