---
uid: "113253"
seealso:
- linkId: "112608"
- linkId: "112621"
- linkId: DevExpress.ExpressApp.SystemModule.WindowTemplateController
- linkId: DevExpress.ExpressApp.SystemModule.WindowTemplateController.CustomizeWindowStatusMessages
- linkId: "113252"
title: 'How to: Customize Window Status Messages (WinForms)'
owner: Vera Ulitina
---
# How to: Customize Window Status Messages (WinForms)

A status bar of a typical Windows Forms XAF application [Window](xref:112608) displays a currently authenticated user name, when the application uses a [Security System](xref:113366).

![HowToCustomizeStatusDefault](~/images/howtocustomizestatusdefault116558.png)

This topic describes how to add a custom status message and how to replace the default message with a custom one.

## Add a Custom Status Message
The [](xref:DevExpress.ExpressApp.SystemModule.WindowTemplateController) is activated in all Windows and updates the current Window status and caption. The `WindowTemplateController` exposes the [WindowTemplateController.CustomizeWindowStatusMessages](xref:DevExpress.ExpressApp.SystemModule.WindowTemplateController.CustomizeWindowStatusMessages) event, which occurs before Window status messages are updated and allows you to modify them. The status messages are a collection of strings in XAF.

To add a status message, create a custom [Window Controller](xref:112621), subscribe to the `CustomizeWindowStatusMessages` event and handle it. Add a custom string to the `StatusMessages` collection in the `CustomizeWindowStatusMessages` event handler.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;
// ...
public class CustomizeWindowController : WindowController {
    protected override void OnActivated() {
        base.OnActivated();
        WindowTemplateController controller = Frame.GetController<WindowTemplateController>();
        controller.CustomizeWindowStatusMessages += Controller_CustomizeWindowStatusMessages;
    }
    private void Controller_CustomizeWindowStatusMessages(object sender,
    CustomizeWindowStatusMessagesEventArgs e) {
        e.StatusMessages.Add("My custom status message");
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        WindowTemplateController controller = Frame.GetController<WindowTemplateController>();
        controller.CustomizeWindowStatusMessages -= Controller_CustomizeWindowStatusMessages;
    }
}
```

***

Use the @DevExpress.ExpressApp.Window.IsMain property in the `CustomizeWindowStatusMessages` event handler to create a condition that adds a status message only to the main or a child window.

The following image illustrates a custom status message displayed together with a default message:

![HowToCustomizeStatusCustom1](~/images/howtocustomizestatuscustom1116559.png)

## Replace the Default Status Message
To replace a current status messages collection with a custom one, clear the `StatusMessages` collection before adding a custom message in the `CustomizeWindowStatusMessages` event handler.

# [C#](#tab/tabid-csharp)

```csharp
private void Controller_CustomizeWindowStatusMessages(object sender, 
CustomizeWindowStatusMessagesEventArgs e) {
    e.StatusMessages.Clear();
    e.StatusMessages.Add("My custom status message");
}
```

***

The following image illustrates a displayed custom status message, instead of a default one:

![HowToCustomizeStatusCustom2](~/images/howtocustomizestatuscustom2116560.png)

You can use the [WindowTemplateController.UpdateWindowStatusMessage](xref:DevExpress.ExpressApp.SystemModule.WindowTemplateController.UpdateWindowStatusMessage) method to refresh status messages when required.

> [!NOTE]
> This topic concerns Windows Form applications only.

To put anything besides text messages into the Status Bar, consider [creating a custom window template](xref:112696) or subscribe to the [WindowTemplateController.CustomizeStatusBar](xref:DevExpress.ExpressApp.SystemModule.WindowTemplateController.CustomizeStatusBar) event and access the bar directly. Refer to the [How to: Access the Bar Manager](xref:115213) and [How to: Access the Ribbon Control](xref:115214) articles and the [XtraBars](xref:1199) product documentation.