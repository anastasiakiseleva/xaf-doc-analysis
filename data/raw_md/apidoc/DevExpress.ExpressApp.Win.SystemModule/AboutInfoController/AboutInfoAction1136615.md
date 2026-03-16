---
uid: DevExpress.ExpressApp.Win.SystemModule.AboutInfoController.AboutInfoAction
name: AboutInfoAction
type: Property
summary: Invokes a window that displays the 'About' information on the current application.
syntax:
  content: public PopupWindowShowAction AboutInfoAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.PopupWindowShowAction
    description: A [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) object that is the **About** Action.
seealso:
- linkId: "113445"
---
This Action displays a Detail View for the [](xref:DevExpress.ExpressApp.SystemModule.AboutInfo) class instance. This Detail View contains two View Items: a StaticTextViewItem and StaticImageDetailItem. The StaticTextViewItem displays text provided by the [AboutInfo.AboutInfoString](xref:DevExpress.ExpressApp.SystemModule.AboutInfo.AboutInfoString) property. The StaticImageDetailItem displays the image specified by the [AboutInfo.LogoImageName](xref:DevExpress.ExpressApp.SystemModule.AboutInfo.LogoImageName) property.

![AboutActionWin](~/images/aboutactionwin116183.png)

For more details, refer to the [](xref:DevExpress.ExpressApp.Win.SystemModule.AboutInfoController) class description.