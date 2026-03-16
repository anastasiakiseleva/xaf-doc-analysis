---
uid: DevExpress.ExpressApp.Utils.CaptionHelper.CustomizeConvertCompoundName
name: CustomizeConvertCompoundName
type: Event
summary: Occurs after a call to the [CaptionHelper.ConvertCompoundName](xref:DevExpress.ExpressApp.Utils.CaptionHelper.ConvertCompoundName*) method. Allows you to manually process a compound name that's being converted.
syntax:
  content: public static event EventHandler<CustomizeConvertCompoundNameEventArgs> CustomizeConvertCompoundName
seealso: []
---
Handle this event to provide a custom algorithm for processing compound names. Use the handler's [CustomizeConvertCompoundNameEventArgs.Name](xref:DevExpress.ExpressApp.Utils.CustomizeConvertCompoundNameEventArgs.Name) property to get the compound name to be processed. Use the handler's [CustomizeConvertCompoundNameEventArgs.Style](xref:DevExpress.ExpressApp.Utils.CustomizeConvertCompoundNameEventArgs.Style) property, to learn how the compound name should be processed. Set the handler's **Handled** parameter to **true**, to cancel the default processing by the **ConvertCompoundName** method.