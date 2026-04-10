## ASP.NET Core Blazor

In XAF ASP.NET Core Blazor applications, shortcuts are available for Actions that appear as Toolbar items and Grid Row Context Menu items.

XAF does not distinguish between the left or right modifier keys: <kbd>Control</kbd>, <kbd>Shift</kbd>, or <kbd>Alt</kbd>.

XAF ASP.NET Core Blazor applications support multiple shortcuts for a single Action. The semicolon symbol separates individual shortcuts and cannot be part of a shortcut.

XAF ASP.NET Core Blazor applications support most of the Windows Forms syntax, but we recommend setting shortcuts in ASP.NET Core Blazor applications as follows:

- Control+Shift+Alt+Windows+O
- Control+Shift+O
- Control+Shift+PageDown
- Control+Shift+ArrowLeft
- Control+Shift+Equal
- Control+Shift+Period
- Shift+O
- Command+O
- Control+O;Command+O

For specific code values (for example, <kbd>Period</kbd>, <kbd>Comma</kbd>, or <kbd>Slash</kbd>), refer to the following list: [Keyboard Event Code Values (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_code_values.)

The following table contains default shortcuts you can use to execute Actions in XAF ASP.NET Core Blazor applications:

| Action | Shortcut |
|---|---|
| [DeleteAction](xref:DevExpress.ExpressApp.SystemModule.DeleteObjectsViewController.DeleteAction) | Control+Delete |
| [SaveAction](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.SaveAction) | Control+Shift+S |
| [SaveAndCloseAction](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.SaveAndCloseAction) | Control+Shift+Enter |
| [NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction) | Control+Shift+A |
| [PreviousObjectAction ](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController.PreviousObjectAction) | Control+Alt+ArrowLeft |
| [NextObjectAction ](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController.NextObjectAction) | Control+Alt+ArrowRight |
| [RefreshAction](xref:DevExpress.ExpressApp.SystemModule.RefreshController.RefreshAction) | Control+Shift+R |
| [AcceptAction](xref:DevExpress.ExpressApp.SystemModule.DialogController.AcceptAction) | Control+Shift+Enter |
| [LogonAction](xref:113141#logoncontroller) | Enter |