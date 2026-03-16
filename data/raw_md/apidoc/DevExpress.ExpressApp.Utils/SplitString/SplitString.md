---
uid: DevExpress.ExpressApp.Utils.SplitString
name: SplitString
type: Class
summary: Represents a string which consists of two parts split by a separator.
syntax:
  content: public class SplitString
seealso:
- linkId: DevExpress.ExpressApp.Utils.SplitString._members
  altText: SplitString Members
- linkId: "113252"
---
This **SplitString** class represents a string calculated from two substrings divided by a separator. The **SplitString** exposes properties to modify each part separately, or the whole string at once.

The string represented by the **SplitString** class is exposed via the [SplitString.Text](xref:DevExpress.ExpressApp.Utils.SplitString.Text) property. 
Its value is calculated by concatenating the values of the [SplitString.FirstPart](xref:DevExpress.ExpressApp.Utils.SplitString.FirstPart), [SplitString.Separator](xref:DevExpress.ExpressApp.Utils.SplitString.Separator) and [SplitString.SecondPart](xref:DevExpress.ExpressApp.Utils.SplitString.SecondPart) string properties. However, if one of the parts is empty or undefined, the **Separator** is omitted. You can also manually assign a custom value to the **Text** property. In this instance, the values of the **FirstPart**, **Separator** and **SecondPart** properties are ignored.

For an example of using **SplitString**, refer to the [How to: Customize a Window Caption](xref:113252) topic.

> [!NOTE]
> **XAF** uses instances of the **SplitString** class to represent [Window](xref:112608) captions. For additional information, see the [](xref:DevExpress.ExpressApp.SystemModule.WindowTemplateController) class description.