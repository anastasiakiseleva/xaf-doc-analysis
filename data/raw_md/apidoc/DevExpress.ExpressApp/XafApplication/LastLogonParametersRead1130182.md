---
uid: DevExpress.ExpressApp.XafApplication.LastLogonParametersRead
name: LastLogonParametersRead
type: Event
summary: Occurs after loading the last logon parameters from the settings storage to the logon object.
syntax:
  content: public event EventHandler<LastLogonParametersReadEventArgs> LastLogonParametersRead
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.LastLogonParametersReading
- linkId: DevExpress.ExpressApp.XafApplication.LastLogonParametersWriting
- linkId: DevExpress.ExpressApp.XafApplication.CreateCustomLogonParameterStore
- linkId: DevExpress.ExpressApp.Utils.ICustomObjectSerialize
- linkId: "404264"
---
A logon Window contains a [View](xref:112611) that displays [Security System](xref:113366)'s logon parameters. In a Windows Forms application, this View shows the last user's parameters. To load these parameters, XAF creates a storage object. It loads logon parameters from the _LogonParameters_ file. When the application is launched for the first time, the logon parameters storage is empty. ASP.NET Core Blazor applications do not create the last user's parameters storage by default.

You can handle the `LastLogonParametersRead` event to customize the loaded logon parameters. Use the handler's [LastLogonParametersReadEventArgs.LogonObject](xref:DevExpress.ExpressApp.LastLogonParametersReadEventArgs.LogonObject) parameter to modify the logon parameters loaded from the settings storage.

The following code snippet displays the "Guest" user name when the application is launched for the first time.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
// ...

namespace MySolution.Module;

public sealed partial class MySolutionModule : ModuleBase {
    // ...
    public override void Setup(XafApplication application) {
        base.Setup(application);
        application.LastLogonParametersRead += Application_LastLogonParametersRead;
    }
    private void Application_LastLogonParametersRead(object sender, LastLogonParametersReadEventArgs e) {
        if (e.LogonObject is AuthenticationStandardLogonParameters standardLogonParameters && string.IsNullOrEmpty(standardLogonParameters.UserName)) {
            standardLogonParameters.UserName = "Guest";
        }
    }
    // ...
}
```
***

> [!NOTE]
> The same task can be accomplished via handling the [XafApplication.LastLogonParametersReading](xref:DevExpress.ExpressApp.XafApplication.LastLogonParametersReading) and modifying the logon parameters before they are loaded from the settings storage. Additionally, you can handle the [XafApplication.LastLogonParametersWriting](xref:DevExpress.ExpressApp.XafApplication.LastLogonParametersWriting) event to specify the custom logic applied when saving logon parameters to the settings storage.

When using custom logon parameters, you can implement the [](xref:DevExpress.ExpressApp.Utils.ICustomObjectSerialize) interface. The logon parameters saving and loading can be handled in the [ICustomObjectSerialize.ReadPropertyValues](xref:DevExpress.ExpressApp.Utils.ICustomObjectSerialize.ReadPropertyValues(DevExpress.ExpressApp.Utils.SettingsStorage)) and [ICustomObjectSerialize.WritePropertyValues](xref:DevExpress.ExpressApp.Utils.ICustomObjectSerialize.WritePropertyValues(DevExpress.ExpressApp.Utils.SettingsStorage)) methods.
