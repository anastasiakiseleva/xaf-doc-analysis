---
uid: DevExpress.ExpressApp.Utils.CustomizeConvertCompoundNameEventArgs
name: CustomizeConvertCompoundNameEventArgs
type: Class
summary: Arguments passed to the [CaptionHelper.CustomizeConvertCompoundName](xref:DevExpress.ExpressApp.Utils.CaptionHelper.CustomizeConvertCompoundName) event.
syntax:
  content: 'public class CustomizeConvertCompoundNameEventArgs : HandledEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.Utils.CustomizeConvertCompoundNameEventArgs._members
  altText: CustomizeConvertCompoundNameEventArgs Members
---
The **CustomizeConvertCompoundName** event occurs after a call to the [CaptionHelper.ConvertCompoundName](xref:DevExpress.ExpressApp.Utils.CaptionHelper.ConvertCompoundName*) method, and allows you to manually process a compound name that's being converted.

The **CustomizeConvertCompoundNameEventArgs** class exposes two properties which represent the parameters passed to the **ConvertCompoundName** method. The [CustomizeConvertCompoundNameEventArgs.Name](xref:DevExpress.ExpressApp.Utils.CustomizeConvertCompoundNameEventArgs.Name) property specifies the compound name to be processed. The [CustomizeConvertCompoundNameEventArgs.Style](xref:DevExpress.ExpressApp.Utils.CustomizeConvertCompoundNameEventArgs.Style) property specifies how the compound name should be processed.