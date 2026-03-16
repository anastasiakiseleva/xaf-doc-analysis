---
uid: DevExpress.ExpressApp.LastLogonParametersWritingEventArgs
name: LastLogonParametersWritingEventArgs
type: Class
summary: Represents arguments passed to an application's [XafApplication.LastLogonParametersWriting](xref:DevExpress.ExpressApp.XafApplication.LastLogonParametersWriting) event.
syntax:
  content: 'public class LastLogonParametersWritingEventArgs : HandledEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.LastLogonParametersWritingEventArgs._members
  altText: LastLogonParametersWritingEventArgs Members
---
The **LastLogonParametersWritingEventArgs** class declares properties specific to the [XafApplication.LastLogonParametersReading](xref:DevExpress.ExpressApp.XafApplication.LastLogonParametersReading) event. This event is designed to customize the logon parameters before saving. Use the handler's [LastLogonParametersReadEventArgs.LogonObject](xref:DevExpress.ExpressApp.LastLogonParametersReadEventArgs.LogonObject) parameter to specify the current logon parameters. The **SettingsStorage** parameter allows you to use methods of the storage to save the logon parameters to a specified location.

This class is inherited from the **HandleEventArgs** class, so, you can use the handler's **Handled** parameter to prevent repeated saving of the current logon parameters by the system.