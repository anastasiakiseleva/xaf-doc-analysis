---
uid: DevExpress.ExpressApp.Utils.CaptionHelper.ConvertCompoundName(System.String)
name: ConvertCompoundName(String)
type: Method
summary: Converts a compound name so that the words forming the name are separated by white spaces.
syntax:
  content: public static string ConvertCompoundName(string name)
  parameters:
  - id: name
    type: System.String
    description: A string representing the compound name that will be converted.
  return:
    type: System.String
    description: A string representing the processed compound name.
seealso: []
---
Compound names consist of several capitalized words glued together. Examples of such names are **BusinessClass**, **RestoreDefaultSettings**, **MyApplicationModule** and so on. This **ConvertCompoundName** method overload separates the words forming a compound name with white spaces. So, for example, the **RestoreDefaultSettings** compound name would be converted to **Restore Default Settings**.

The **ConvertCompoundName** method raises the [CaptionHelper.CustomizeConvertCompoundName](xref:DevExpress.ExpressApp.Utils.CaptionHelper.CustomizeConvertCompoundName) event, which allows you to manually process a compound name that's being converted.