---
uid: DevExpress.ExpressApp.Win.SystemModule.AboutInfoController
name: AboutInfoController
type: Class
summary: Represents a [](xref:DevExpress.ExpressApp.WindowController) descendant that contains the **About** Action.
syntax:
  content: 'public class AboutInfoController : WindowController'
seealso:
- linkId: DevExpress.ExpressApp.Win.SystemModule.AboutInfoController._members
  altText: AboutInfoController Members
- linkId: DevExpress.ExpressApp.Win.SystemModule.AboutInfoController.AboutInfoAction
- linkId: "113445"
---
The **AboutInfoController** Controller contains the **About** Action. This Action invokes a popup window that shows information about the current Windows Forms application. This information is represented by a Detail View generated for an instance of the [](xref:DevExpress.ExpressApp.SystemModule.AboutInfo) class. This Detail View contains two View Items: a **StaticTextViewItem** and **StaticImageDetailItem**. The **StaticTextViewItem** displays text provided by the [AboutInfo.AboutInfoString](xref:DevExpress.ExpressApp.SystemModule.AboutInfo.AboutInfoString) property. The **StaticImageDetailItem** displays the image specified by the [AboutInfo.LogoImageName](xref:DevExpress.ExpressApp.SystemModule.AboutInfo.LogoImageName) property.

![AboutActionWin](~/images/aboutactionwin116183.png)

By default, the **AboutInfo.LogoImageName** and **AboutInfo.AboutInfoString** properties are set to the values of the **Logo** and **AboutInfoString** properties of the Application Model's **Application** node, respectively. To customize the 'About' information, you can change the **Application** node's property values in the Model Editor, or set the required values for the **AboutInfo** object's properties in code.

If you need a custom View to be displayed by the **About** Action, customize the AboutInfo Detail View in the Model Editor. For this purpose, remove the "AboutText" and "Logo" View Items and add custom ones.