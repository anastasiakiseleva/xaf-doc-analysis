---
uid: DevExpress.ExpressApp.Utils.CaptionHelper.ConvertCompoundName(System.String,DevExpress.ExpressApp.Utils.CompoundNameConvertStyle)
name: ConvertCompoundName(String, CompoundNameConvertStyle)
type: Method
summary: Converts a compound name according to the specified [](xref:DevExpress.ExpressApp.Utils.CompoundNameConvertStyle) mode.
syntax:
  content: public static string ConvertCompoundName(string name, CompoundNameConvertStyle style)
  parameters:
  - id: name
    type: System.String
    description: A string representing the compound name that will be converted.
  - id: style
    type: DevExpress.ExpressApp.Utils.CompoundNameConvertStyle
    description: A [](xref:DevExpress.ExpressApp.Utils.CompoundNameConvertStyle) enumeration value specifying how the compound name will be processed.
  return:
    type: System.String
    description: A string representing the processed compound name.
seealso: []
---
Compound names consist from several capitalized words joined together. Examples of such names are **BusinessClass**, **RestoreDefaultSettings**, **MyApplicationModule** and so on. The **ConvertCompoundName** method is used to split these names into several words, according to the specified **CompoundNameConvertStyle** mode.

The **ConvertCompoundName** method raises the [CaptionHelper.CustomizeConvertCompoundName](xref:DevExpress.ExpressApp.Utils.CaptionHelper.CustomizeConvertCompoundName) event, which allows you to manually process a compound name that's being converted.