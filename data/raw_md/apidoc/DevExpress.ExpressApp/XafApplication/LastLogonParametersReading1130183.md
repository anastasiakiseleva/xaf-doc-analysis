---
uid: DevExpress.ExpressApp.XafApplication.LastLogonParametersReading
name: LastLogonParametersReading
type: Event
summary: Occurs before loading the last logon parameters from the settings storage to the logon object.
syntax:
  content: public event EventHandler<LastLogonParametersReadingEventArgs> LastLogonParametersReading
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.LastLogonParametersRead
- linkId: DevExpress.ExpressApp.XafApplication.LastLogonParametersWriting
- linkId: DevExpress.ExpressApp.XafApplication.CreateCustomLogonParameterStore
- linkId: DevExpress.ExpressApp.Utils.ICustomObjectSerialize
- linkId: "404264"
---
A logon Window contains a [View](xref:112611) which represents a [Security System](xref:113366)'s logon parameters. In a Windows Forms application, this View shows the last user's parameters. To load these parameters, a special storage object is created. It loads logon parameters from the _LogonParameters_ file. When the application is launched for the first time, the logon parameters storage is empty. ASP.NET Core Blazor applications do not create the last user's parameters storage by default.

You can handle the `LastLogonParametersReading` event to load custom logon parameters. Use the handler's [LastLogonParametersReadingEventArgs.SettingsStorage](xref:DevExpress.ExpressApp.LastLogonParametersReadingEventArgs.SettingsStorage) parameter to load the last logon parameters to the object specified by the [LastLogonParametersReadingEventArgs.LogonObject](xref:DevExpress.ExpressApp.LastLogonParametersReadingEventArgs.LogonObject) parameter. The example below demonstrates how to set the user name shown when the application is launched for the first time to "Guest".

In a Windows Forms application project's _Program.cs_ file:

# [C#](#tab/tabid-csharp)

```csharp
static void Main() {
    // ...
    winApplication.LastLogonParametersReading += 
        new EventHandler<LastLogonParametersReadingEventArgs>(
            winApplication_LastLogonParametersReading);
    // ...
    winApplication.Setup();
    winApplication.Start();
    // ...
}
static void winApplication_LastLogonParametersReading(
    object sender, LastLogonParametersReadingEventArgs e) {
    if (string.IsNullOrEmpty(e.SettingsStorage.LoadOption("", "UserName"))) {
        e.SettingsStorage.SaveOption("", "UserName", "Guest");
    }
}
```
***

> [!NOTE]
> The same task can be accomplished by handling the [XafApplication.LastLogonParametersRead](xref:DevExpress.ExpressApp.XafApplication.LastLogonParametersRead) and modifying the logon parameters which are already loaded from the settings storage. Additionally, you can handle the [XafApplication.LastLogonParametersWriting](xref:DevExpress.ExpressApp.XafApplication.LastLogonParametersWriting) event to specify the custom logic applied when saving logon parameters to the settings storage.

Default parameter loading can be prevented by setting the handler's `Handled` parameter to `true`. When you set this parameter to `true` and add no other code to the `LastLogonParametersReading` event handler, the logon parameters shown in the logon window will always be empty. If it is required to implement a custom logic, add the corresponding code to the event handler and set `Handled` to `true`, to indicate that it is not required to perform the default process of loading the last logon parameters from the settings storage to the logon object.

When using custom logon parameters, you can implement the [](xref:DevExpress.ExpressApp.Utils.ICustomObjectSerialize) interface. The logon parameters saving and loading can be handled in the [ICustomObjectSerialize.ReadPropertyValues](xref:DevExpress.ExpressApp.Utils.ICustomObjectSerialize.ReadPropertyValues(DevExpress.ExpressApp.Utils.SettingsStorage)) and [ICustomObjectSerialize.WritePropertyValues](xref:DevExpress.ExpressApp.Utils.ICustomObjectSerialize.WritePropertyValues(DevExpress.ExpressApp.Utils.SettingsStorage)) methods.
