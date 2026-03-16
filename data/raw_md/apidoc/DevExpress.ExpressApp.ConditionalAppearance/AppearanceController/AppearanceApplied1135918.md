---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.AppearanceApplied
name: AppearanceApplied
type: Event
summary: Occurs after the conditional appearance is applied to the target UI element.
syntax:
  content: public event EventHandler<ApplyAppearanceEventArgs> AppearanceApplied
seealso: []
---
The AppearanceController applies conditional appearance rules declared for the target UI element. The Controller collects them from the Application Model, filters them leaving only those that satisfy the specified conditions and criteria, and combines them to the AppearanceObject according the specified priority. The AppearanceObject specifies whether to enable/disable the target item, make it invisible/visible, set the item's background color, font color or font style. If you need to change one or several of these appearance settings after they have been applied, handle the **AppearanceApplied** event. In this instance, if other appearance settings specified by the AppearanceObject has been applied, you will leave them as is. To get the target item, use the event handler's [ApplyAppearanceEventArgs.Item](xref:DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.Item), [ApplyAppearanceEventArgs.ItemName](xref:DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.ItemName) and [ApplyAppearanceEventArgs.ItemType](xref:DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.ItemType) parameters. To access the conditional appearance applied, use the event handler's [ApplyAppearanceEventArgs.AppearanceObject](xref:DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.AppearanceObject) parameter. To get the context object(s), use the [ApplyAppearanceEventArgs.ContextObjects](xref:DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.ContextObjects) parameter. To customize the applied appearance, access the target item and cast it by one of the following interfaces:

* [](xref:DevExpress.ExpressApp.Editors.IAppearanceFormat)
    
    Allows you to set the back color, font color and font style of the UI element supporting this interface.
* [](xref:DevExpress.ExpressApp.Editors.IAppearanceEnabled)
    
    Allows you to disable/enable the UI element supporting this interface.
* [](xref:DevExpress.ExpressApp.Editors.IAppearanceVisibility)
    
    Allows you to hide/show the UI element supporting this interface.

Casting the target item to one of the interfaces above, you can reset the applied appearance settings. For this purpose, use the corresponding interface methods.

If these interfaces do not provide the required appearance settings, use the item's properties directly. To learn which items may present as appearance items, see the table in the [AppearanceController.CustomApplyAppearance](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.CustomApplyAppearance) event description.

To apply a custom conditional appearance, handle the [AppearanceController.CustomApplyAppearance](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.CustomApplyAppearance) event. Set the _Handled_ event handler parameter to **true** so that the appearance settings specified by the AppearanceObject do not override your custom appearance.

Refer to the [How to: Customize the Conditional Appearance Module Behavior](xref:113374) topic to see an example of handling this event.