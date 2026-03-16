---
uid: DevExpress.ExpressApp.Win.SystemModule.IHtmlFormattingSupport
name: IHtmlFormattingSupport
type: Interface
summary: Declares members implemented by Windows Forms [List Editors](xref:113189) and [View Items](xref:112612) that support HTML formatting of the display text.
syntax:
  content: public interface IHtmlFormattingSupport
seealso:
- linkId: DevExpress.ExpressApp.Win.SystemModule.IHtmlFormattingSupport._members
  altText: IHtmlFormattingSupport Members
---
Certain Windows Forms controls can display an HTML formatted text, either according to the HTML tags or as a plain text. **XAF** provides an easy way to enable HTML formatting in List Editors and View Items that use such controls. To enable HTML formatting, set the [IModelOptionsEnableHtmlFormatting.EnableHtmlFormatting](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsEnableHtmlFormatting.EnableHtmlFormatting) property of the [Application Model](xref:112580)'s **Options** node to **true**. This affects all the List Editors and View Items that implement the **IHtmlFormattingSupport** interface.

The **IHtmlFormattingSupport** interface exposes a single [IHtmlFormattingSupport.SetHtmlFormattingEnabled](xref:DevExpress.ExpressApp.Win.SystemModule.IHtmlFormattingSupport.SetHtmlFormattingEnabled(System.Boolean)) method that enables or disables HTML formatting.

When implementing a custom List Editor or a View Item, support this interface if the control you are using can format the display text according to Hyper Text Markup Language.

To learn more about the HTML Formatting feature, refer to the [How to: Apply HTML Formatting to Windows Forms XAF UI Elements](xref:113130) topic.