---
uid: DevExpress.ExpressApp.Utils.ICustomObjectSerialize
name: ICustomObjectSerialize
type: Interface
summary: Declares methods implemented by classes that interact with the settings storage.
syntax:
  content: public interface ICustomObjectSerialize
seealso:
- linkId: DevExpress.ExpressApp.Utils.ICustomObjectSerialize._members
  altText: ICustomObjectSerialize Members
- linkId: DevExpress.ExpressApp.XafApplication.LastLogonParametersReading
- linkId: DevExpress.ExpressApp.XafApplication.LastLogonParametersRead
- linkId: DevExpress.ExpressApp.XafApplication.LastLogonParametersWriting
- linkId: DevExpress.ExpressApp.XafApplication.CreateCustomLogonParameterStore
---
The `ICustomObjectSerialize` interface exposes two methods.

The [ICustomObjectSerialize.ReadPropertyValues](xref:DevExpress.ExpressApp.Utils.ICustomObjectSerialize.ReadPropertyValues(DevExpress.ExpressApp.Utils.SettingsStorage)) method handles loading the values from the settings storage.

You can implement the `ICustomObjectSerialize` interface in an `AuthenticationStandardLogonParameters` descendant, to customize the process of loading and saving logon parameters. The code below enables users to choose whether to input a password each time the Logon [Window](xref:112608) is displayed or input a password once and remember it in the logon parameters storage.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.DC;
using DevExpress.ExpressApp.Security;
using DevExpress.ExpressApp.Utils;
// ...
[DomainComponent]
public class MyLogonParameters : AuthenticationStandardLogonParameters, ICustomObjectSerialize {
    private bool rememberPassword;
    public bool RememberPassword {
        get { 
           return rememberPassword; 
        }
        set { 
            rememberPassword = value;
        }
    }
    public void ReadPropertyValues(SettingsStorage storage) {
        UserName = storage.LoadOption("", "UserName");
        Password = storage.LoadOption("", "Password");
        RememberPassword = storage.LoadBoolOption("", "RememberPassword", false);
    }
    public void WritePropertyValues(SettingsStorage storage) {
        storage.SaveOption("", "UserName", UserName);
        storage.SaveOption("", "Password", RememberPassword ? Password : "");
        storage.SaveOption("", "RememberPassword", RememberPassword.ToString());
    }
}
```
***

> [!NOTE]
> You may need to add a reference to the _DevExpress.ExpressApp.Security.<:xx.x:>.dll_ assembly.

Take note of the [ICustomObjectSerialize.ReadPropertyValues](xref:DevExpress.ExpressApp.Utils.ICustomObjectSerialize.ReadPropertyValues(DevExpress.ExpressApp.Utils.SettingsStorage)) and [ICustomObjectSerialize.WritePropertyValues](xref:DevExpress.ExpressApp.Utils.ICustomObjectSerialize.WritePropertyValues(DevExpress.ExpressApp.Utils.SettingsStorage)) methods implementation. In the `ReadPropertyValues` method, the logon parameter values are loaded via the `SettingsStorage.LoadOption` and `SettingsStorage.LoadBoolOption` methods. In the `WritePropertyValues` method, the logon parameter values are saved via the `SettingsStorage.SaveOption` method. Non-string values should be converted to strings before saving. The `RememberPassword` property will be displayed in the Logon Window, together with the `UserName` and `Password` properties exposed by the `AuthenticationStandardLogonParameters` ancestor class. However, the `RememberPassword` property is not included in the authentication process.

To use custom logon parameters in the XAF application, set the provider's @DevExpress.ExpressApp.Security.AuthenticationStandardProviderOptions.LogonParametersType option to `CustomLogonParameters` in the `AddPasswordAuthentication` method call.

**Files:** _SolutionName.Blazor.Server\Startup.cs_, _SolutionName.MiddleTier\Startup.cs_

[!codesnippet-csharp[dx-examples](xaf-custom-logon-parameters/CS/EF/EFCoreCustomLogonAll.Blazor.Server/Startup.cs?line=66,67,72-76)]
```csharp
builder.Security
// ...
    .UseIntegratedMode(options => {
    // ...
    })
    .AddPasswordAuthentication(options => {
        options.IsSupportChangePassword = true;
        options.LogonParametersType = typeof(CustomLogonParameters);
    });
```

Run the application.

![LogonSavePassword](~/images/logonsavepassword116599.png)

> [!NOTE]
> In an XAF Windows Forms application, the logon parameters are stored in the _LogonParameters_ file. Blazor applications do not store logon parameters. You can change this behavior by handling the [](xref:DevExpress.ExpressApp.XafApplication.CreateCustomLogonParameterStore) event.

In some scenarios, you may need to store non-string logon parameters. If a persistent object is used as a logon parameter, you can store the string representation of its [BaseObject.Oid](xref:DevExpress.Persistent.BaseImpl.BaseObject.Oid) property or another property that has a unique value (for example, [PermissionPolicyUser.UserName](xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser.UserName)).

You can handle the [XafApplication.LastLogonParametersRead](xref:DevExpress.ExpressApp.XafApplication.LastLogonParametersRead), [XafApplication.LastLogonParametersReading](xref:DevExpress.ExpressApp.XafApplication.LastLogonParametersReading) and [XafApplication.LastLogonParametersWriting](xref:DevExpress.ExpressApp.XafApplication.LastLogonParametersWriting) events to customize the process of saving and loading the logon parameters, instead of the approach described in this topic. Additionally, you can use custom settings storage by handling the [XafApplication.CreateCustomLogonParameterStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomLogonParameterStore) event.