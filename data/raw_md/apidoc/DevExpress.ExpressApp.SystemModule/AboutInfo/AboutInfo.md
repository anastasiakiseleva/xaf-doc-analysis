---
uid: DevExpress.ExpressApp.SystemModule.AboutInfo
name: AboutInfo
type: Class
summary: Provides information about the current application.
syntax:
  content: |-
    [DomainComponent]
    public class AboutInfo
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.AboutInfo._members
  altText: AboutInfo Members
---
`AboutInfo` is a singleton. Use the [AboutInfo.Instance](xref:DevExpress.ExpressApp.SystemModule.AboutInfo.Instance) property, to access the object. The following properties of this object represent the "About" information on the current application:
* [AboutInfo.Company](xref:DevExpress.ExpressApp.SystemModule.AboutInfo.Company)
* [AboutInfo.Copyright](xref:DevExpress.ExpressApp.SystemModule.AboutInfo.Copyright)
* [AboutInfo.Description](xref:DevExpress.ExpressApp.SystemModule.AboutInfo.Description)
* [AboutInfo.ProductName](xref:DevExpress.ExpressApp.SystemModule.AboutInfo.ProductName)
* [AboutInfo.Version](xref:DevExpress.ExpressApp.SystemModule.AboutInfo.Version).

The [AboutInfo.AboutInfoString](xref:DevExpress.ExpressApp.SystemModule.AboutInfo.AboutInfoString) property provides summary information by concatenating the values of the other properties.

The [AboutInfo.LogoImageName](xref:DevExpress.ExpressApp.SystemModule.AboutInfo.LogoImageName) property stores the logo image name in applications.

In Windows Forms applications, the [](xref:DevExpress.ExpressApp.Win.SystemModule.AboutInfoController)'s **About** Action invokes a Detail View with two Detail View Items: the `StaticImageDetailItem` and `StaticTextViewItem`. The `StaticTextViewItem` shows the text provided by the `AboutInfo` object's `AboutInfoString` property. The `StaticImageDetailItem` displays the image specified by the [AboutInfo.LogoImageName](xref:DevExpress.ExpressApp.SystemModule.AboutInfo.LogoImageName) property. The following image demonstrates the **About** Action with the invoked informational pop-up window.

![AboutActionWin](~/images/aboutactionwin116183.png)

To learn how to customize the information provided by the `AboutInfo` object, refer to the description of its properties.