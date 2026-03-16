---
uid: "113475"
seealso: []
title: Logon Form Controllers and Actions
owner: Ekaterina Kiseleva
---
# Logon Form Controllers and Actions

When you use the [Security System](xref:404204) with the [](xref:DevExpress.ExpressApp.Security.AuthenticationStandard) authentication, the logon window is displayed at startup. This window contains a Detail View of a Logon Parameters object (**AuthenticationStandardLogonParameters** by default, or [custom Logon Parameters](xref:404264)). Controllers are not activated automatically for the logon form for security reasons. This topic describes how to activate your custom Controller for the Logon Form.

## Activate a Controller for the Logon Form

To activate a specific Controller, override the [](xref:DevExpress.ExpressApp.XafApplication) class's **CreateLogonWindowControllers** method, or handle the [XafApplication.CreateCustomLogonWindowControllers](xref:DevExpress.ExpressApp.XafApplication.CreateCustomLogonWindowControllers) event as follows.

# [C#](#tab/tabid-csharp)

```csharp
public sealed partial class MySolutionModule : ModuleBase {
    // ...
    public override void Setup(XafApplication application) {
        base.Setup(application);
        application.CreateCustomLogonWindowControllers += application_CreateCustomLogonWindowControllers;
    }
    private void application_CreateCustomLogonWindowControllers(object sender, CreateCustomLogonWindowControllersEventArgs e) {
        e.Controllers.Add(((XafApplication)sender).CreateController<MyController>());
    }
}
```
***

Certain built-it Controllers (for example, Controllers of the [Validation](xref:113684) and [Conditional Appearance](xref:113286) modules) are active on logon. This enables you to apply appearance and validation rules to the logon parameters object.

## Add a Custom Action to the Logon Form

To add a custom Action to the Logon Form, implement a Controller as shown above. Then add the Action to the Controller and set the Action's category as the [](xref:112804) and [](xref:112816) articles describe.
