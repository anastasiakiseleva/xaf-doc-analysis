---
uid: DevExpress.ExpressApp.LastLogonParametersReadingEventArgs
name: LastLogonParametersReadingEventArgs
type: Class
summary: Provides data for the [XafApplication.LastLogonParametersReading](xref:DevExpress.ExpressApp.XafApplication.LastLogonParametersReading) event.
syntax:
  content: 'public class LastLogonParametersReadingEventArgs : HandledEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.LastLogonParametersReadingEventArgs._members
  altText: LastLogonParametersReadingEventArgs Members
---
The **LastLogonParametersReadingEventArgs** class declares properties specific to the [XafApplication.LastLogonParametersReading](xref:DevExpress.ExpressApp.XafApplication.LastLogonParametersReading) event. This event is designed to load custom logon parameters before passing them to a logon Window. Use the handler's [LastLogonParametersReadingEventArgs.SettingsStorage](xref:DevExpress.ExpressApp.LastLogonParametersReadingEventArgs.SettingsStorage) property to load the last logon parameters to the object specified by the [LastLogonParametersReadingEventArgs.LogonObject](xref:DevExpress.ExpressApp.LastLogonParametersReadingEventArgs.LogonObject) parameter.

This class is inherited from the **HandledEventArgs** class. So, you can use the handler's **Handled** parameter to prevent further loading of the default logon parameters.