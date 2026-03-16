---
uid: DevExpress.ExpressApp.XafApplication.LastLogonParametersWriting
name: LastLogonParametersWriting
type: Event
summary: Occurs before saving the logon [Window](xref:112608)'s logon parameters to the settings storage.
syntax:
  content: public event EventHandler<LastLogonParametersWritingEventArgs> LastLogonParametersWriting
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.LastLogonParametersRead
- linkId: DevExpress.ExpressApp.XafApplication.LastLogonParametersReading
- linkId: DevExpress.ExpressApp.XafApplication.CreateCustomLogonParameterStore
- linkId: DevExpress.ExpressApp.Utils.ICustomObjectSerialize
- linkId: "404264"
---
A logon Window contains a [View](xref:112611) which represents a [Security System](xref:113366)'s logon parameters. In a Windows Forms application, this View shows the last user's parameters. To load these parameters, a special storage object is created. It loads logon parameters from the _LogonParameters_ file. When the application is launched for the first time, the logon parameters storage is empty. ASP.NET Core Blazor applications do not create the last user's parameters storage by default.

You can customize the logon parameters to be saved. For this purpose, handle the `LastLogonParametersWriting` event. This event is raised when the logon is successful. Use the handler's [LastLogonParametersWritingEventArgs.LogonObject](xref:DevExpress.ExpressApp.LastLogonParametersWritingEventArgs.LogonObject) parameter to specify the logon parameters to be saved. Save the customized logon parameters via the object specified by the [LastLogonParametersWritingEventArgs.SettingsStorage](xref:DevExpress.ExpressApp.LastLogonParametersWritingEventArgs.SettingsStorage) parameter. Set  the handler's `Handled` parameter to `true`, to cancel the default operations performed with the settings storage.

An XAF Windows Forms application displays the last authenticated user name in the logon window, by default. So, end-users do not have to retype their user name each time they start the application. But, when the application administrator logs into  the application at an end-user workstation to perform administrative tasks, the saved username is rewritten by the administrator's user name. An end-user will have to type their user name at the next logon. The following example illustrates how to change this behavior, and not  save a particular user name.

The Windows Forms application project's _Program.cs_ file:

# [C#](#tab/tabid-csharp)

```csharp
static void Main() {
    // ...
    winApplication.LastLogonParametersWriting += 
        new EventHandler<LastLogonParametersWritingEventArgs>(
            winApplication_LastLogonParametersWriting);
    // ...
    winApplication.Setup();
    winApplication.Start();
    // ...
}
static void winApplication_LastLogonParametersWriting(
    object sender, LastLogonParametersWritingEventArgs e) {
    if(((AuthenticationStandardLogonParameters)e.LogonObject).UserName != "Admin") {
        e.SettingsStorage.SaveOption(
            "", "UserName", ((AuthenticationStandardLogonParameters)e.LogonObject).UserName);
        e.SettingsStorage.SaveOption(
            "", "Password", ((AuthenticationStandardLogonParameters)e.LogonObject).Password);
    }
    e.Handled = true;
}
```
***

With the code above, the "Admin" user name will not be saved in the _LogonParameters_ file, and the previously saved user name will not be changed. So, end-user will not have to type a user name after the application administrator has logged in to work with the application at the end-user workstation.

Additionally, the password can be saved together with the user name. To enable password saving in the Windows Forms application, add the following code to the `LastLogonParametersWriting` event handler:

# [C#](#tab/tabid-csharp)

```csharp
e.SettingsStorage.SaveOption(
    "", "Password", ((AuthenticationStandardLogonParameters)e.LogonObject).Password);
```
***

> [!NOTE]
> The password is saved to the _LogonParameters_ file as plain text.

When using custom logon parameters, you can implement the [](xref:DevExpress.ExpressApp.Utils.ICustomObjectSerialize) interface. The logon parameters saving and loading can be handled in the [ICustomObjectSerialize.ReadPropertyValues](xref:DevExpress.ExpressApp.Utils.ICustomObjectSerialize.ReadPropertyValues(DevExpress.ExpressApp.Utils.SettingsStorage)) and [ICustomObjectSerialize.WritePropertyValues](xref:DevExpress.ExpressApp.Utils.ICustomObjectSerialize.WritePropertyValues(DevExpress.ExpressApp.Utils.SettingsStorage)) methods.
