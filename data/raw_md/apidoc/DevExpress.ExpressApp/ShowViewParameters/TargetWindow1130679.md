---
uid: DevExpress.ExpressApp.ShowViewParameters.TargetWindow
name: TargetWindow
type: Property
summary: Specifies the type of the [Window](xref:112608) that displays the target [View](xref:112611).
syntax:
  content: public TargetWindow TargetWindow { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.TargetWindow
    description: The type of the target window.
seealso:
- linkId: "112608"
defaultMemberValue: 'Default'
---
The `TargetWindow` property specifies the Window where the @DevExpress.ExpressApp.ShowViewParameters.CreatedView appears. XAF determines the particular target window type based on the combination of the following settings:

* Current [Platform](xref:401675)
* Current [Show View Strategy](xref:DevExpress.ExpressApp.ShowViewStrategyBase) (the `UIType` property value)
* `TargetWindow`
* @DevExpress.ExpressApp.NewWindowTarget

The following tables list window types that display the target View based on the specified property values.

## ASP.NET Core Blazor UI

TargetWindow | UIType = SingleWindowSDI | UIType = TabbedMDI
---------|----------|---------
 `Default` | - If the current Frame is a Nested Frame, the View is displayed in a new modal Window.<br/>In other cases, the View is displayed in the current Window (Frame). | - If the current Frame is a nested frame or the current Window is a Popup Window, the View is displayed in a new modal Window.<br/>In other cases, the View is displayed in a new tab in the main Window.
 `Current` | The View is displayed in the current Window (Frame). | The View is displayed in the current Window (Frame).<br/>If the current Window is the main Window, the View is displayed in a new tab in the main Window.
 `NewWindow` | The View is displayed in a new modal Window. | - If the @DevExpress.ExpressApp.NewWindowTarget property is set to `Default` or `MdiChild`, the View is displayed in a new tab in the main Window.<br/> - If the @DevExpress.ExpressApp.NewWindowTarget property is set to `Separate`, the View is displayed in a new modal Window.
 `NewModalWindow` | The View is displayed in a new modal Window. | The View is displayed in a new modal Window.

When the application displays the target view in a modal Window, the Window layout and appearance is defined by the [PopupWindowTemplate](xref:403450#popup-window-template-popupwindowtemplate) context. The system adds a @DevExpress.ExpressApp.SystemModule.DialogController to the Window's [Frame.Controllers](xref:DevExpress.ExpressApp.Frame.Controllers) collection.

## Windows Forms

TargetWindow | UIType = SingleWindowSDI or UIType = MultipleWindowSDI  | UIType = StandardMDI or UIType = TabbedMDI
---------|----------|---------
 `Default` | If the current Frame is a Nested Frame, the behavior is equivalent to the `NewModalWindow` option.<br/>**SingleWindowSDI**:<br/>If the current Window is the main Window, the behavior is equivalent to the `NewWindow` option.<br/>In other cases, the View is displayed in the current Window (Frame).<br/>**MultipleWindowSDI**:<br/>The behavior depends on the View:<br/> - If the current View is a Detail View, the new Window displays the View template context.<br/> - If the current View is a List View, the current Window (Frame) displays the target View.| - If the current Frame is a nested frame or the current Window is a Popup Window, the View is displayed in a new modal Window.<br/> In other cases, the behavior is equivalent to the `NewWindow` option.
 `Current` | The View is displayed in the current Window (Frame).| The View is displayed in the current Window (Frame).<br/> If the current Window is an [Explorer Window](xref:DevExpress.ExpressApp.Win.WinShowViewStrategyBase.Explorers), the behavior is equivalent to the `NewWindow` option.
 `NewWindow` | The View is displayed in a new separate Window. | - If the @DevExpress.ExpressApp.NewWindowTarget property is set to `Default` or `MdiChild`, the View is displayed in a new MDI child Window (in the `StandardMDI` UI) or a new tab (in the `TabbedMDI` UI) in the main Window.<br/>- If the @DevExpress.ExpressApp.NewWindowTarget property is set to `Separate`, the View is displayed in a new separate Window.
 `NewModalWindow` | The View is displayed in a new modal Window. |The View is displayed in a new modal Window.


> [!note]
> In ASP.NET Core Blazor applications, if you use @DevExpress.ExpressApp.ShowViewParameters to display a new window, the application does not refresh the original View after you close the window. In contrast, windows that you create with @DevExpress.ExpressApp.Actions.PopupWindowShowAction update the parent View when you close them.