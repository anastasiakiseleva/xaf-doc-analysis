---
uid: DevExpress.ExpressApp.Utils.CaptionHelper.RemoveAcceleratorSymbol
name: RemoveAcceleratorSymbol
type: Property
summary: Specifies whether the [CaptionHelper.GetLocalizedText](xref:DevExpress.ExpressApp.Utils.CaptionHelper.GetLocalizedText*) method removes the ampersand character that displays accelerator keys in captions.
syntax:
  content: public static bool RemoveAcceleratorSymbol { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true`, to allow the `GetLocalizedText` method to remove the ampersand character that displays accelerator keys in captions; otherwise, `false`.'
seealso: []
---
You do not need to use this property. It is automatically set to the correct value depending on the type of the current application.

In XAF ASP.NET Core Blazor applications, where accelerator keys are not supported, the `RemoveAcceleratorSymbol` property is set to `true`.

In XAF Windows Forms applications, the `RemoveAcceleratorSymbol` property is set to `false`. It allows you to use accelerator keys in dialogs.